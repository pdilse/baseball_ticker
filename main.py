import requests
import queue
import RPi.GPIO as gpio
from bs4 import BeautifulSoup
from ticker import Ticker
from rpi_lcd import LCD

button = 21
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
    pass


def reload_games(channel):
    queue.put(1)


def destroy():
    gpio.cleanup()
    lcd.clear()


if __name__ == '__main__':
    main()
