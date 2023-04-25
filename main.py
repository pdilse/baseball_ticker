import requests
import threading
import queue
import time
import RPi.GPIO as gpio
from bs4 import BeautifulSoup
from ticker import Ticker
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

            time.sleep(5)
            event.set()
            loading_thread.join()
            button_enabled = True
            ticker.update_with_games([])
        except KeyboardInterrupt:
            destroy()
            exit()


def get_game_data():
    # url = "https://www.baseball-reference.com/boxes/"
    #
    # try:
    #     response = requests.get(url)
    #     soup = BeautifulSoup(response.text, 'html.parser')
    #     games = soup.find_all("div", ["game_summary"])
    #     print(f"{len(games)} games")
    # except requests.exceptions.ConnectionError:
    #     print("connection error")
    return []


def get_team_abbreviation(team):
    teams = {
        "Arizona Diamondbacks": "ARI",
        "Atlanta Braves": "ATL",
        "Baltimore Orioles": "BAL",
        "Boston Red Sox": "BOS",
        "Chicago Cubs": "CHC",
        "Chicago White Sox": "CHW",
        "Cincinnati Reds": "CIN",
        "Cleveland Guardians": "CLE",
        "Colorado Rockies": "COL",
        "Detroit Tigers": "DET",
        "Miami Marlins": "FLA",
        "Houston Astros": "HOU",
        "Kansas City Royals": "KAN",
        "Los Angeles Angels": "LAA",
        "Los Angeles Dodgers": "LAD",
        "Milwaukee Brewers": "MIL",
        "Minnesota Twins": "MIN",
        "New York Mets": "NYM",
        "New York Yankees": "NYY",
        "Oakland Athletics": "OAK",
        "Philadelphia Phillies": "PHI",
        "Pittsburgh Pirates": "PIT",
        "San Francisco Giants": "SF",
        "Seattle Mariners": "SEA",
        "St. Louis Cardinals": "STL",
        "Tampa Bay Rays": "TB",
        "Texas Rangers": "TEX",
        "Toronto Blue Jays": "TOR",
        "Washington Nationals": "WAS"
    }

    return teams[team]


def reload_games(channel):
    if button_enabled and queue.empty():
        queue.put(1)


def destroy():
    gpio.cleanup()
    lcd.clear()


if __name__ == '__main__':
    main()
