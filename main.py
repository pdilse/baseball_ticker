import requests
import threading
import queue
import RPi.GPIO as gpio
from bs4 import BeautifulSoup
from ticker import Ticker
from game import Game
from rpi_lcd import LCD

button = 21
button_enabled = False
lcd = LCD()
queue = queue.Queue()


def main():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    gpio.setup(button, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    gpio.add_event_detect(button, gpio.BOTH, callback=reload_games)
    ticker = Ticker(queue, lcd)

    while True:
        try:
            global button_enabled
            button_enabled = False
            event = threading.Event()
            loading_thread = threading.Thread(target=ticker.display_loading, args=(event,))
            loading_thread.start()
            games = get_game_data()
            event.set()
            loading_thread.join()
            button_enabled = True

            if games:
                ticker.update_with_games(games)
            else:
                ticker.update_with_error()
        except KeyboardInterrupt:
            destroy()
            exit()


def get_game_data():
    url = "https://www.baseball-reference.com/boxes/"
    games = []

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        team_rows = soup.select("div.game_summary tr.loser,tr.winner")
        i = 0

        while i < len(team_rows):
            away_row = team_rows[i]
            home_row = team_rows[i + 1]
            i += 2

            away_team, away_score = get_team_and_score(away_row)
            home_team, home_score = get_team_and_score(home_row)
            game = Game(away_team, home_team, away_score, home_score)
            games.append(game)
    except requests.exceptions.ConnectionError:
        print("connection error")
    finally:
        return games


def get_team_and_score(row):
    cells = row.find_all("td")
    return cells[0].getText(), cells[1].getText()


def reload_games(channel):
    if button_enabled and queue.empty():
        queue.put(1)


def destroy():
    gpio.cleanup()
    lcd.clear()


if __name__ == '__main__':
    main()
