import time


class Ticker:
    def __init__(self, queue, lcd):
        self.games = []
        self.queue = queue
        self.lcd = lcd

    def display_loading(self, event):
        self.games = []
        i = 1

        while True:
            self.lcd.text(f"Loading{'.' * i}", 1)
            self.lcd.text("", 2)

            if i < 3:
                i += 1
            else:
                i = 1

            time.sleep(0.5)

            if event.is_set():
                self.lcd.text("", 1)
                break

    def update_with_games(self, games):
        self.games = games
        i = 0

        while True:
            if self.queue.empty():
                self.lcd.text(self.games[i].abbreviation(False), 1)
                self.lcd.text(self.games[i].abbreviation(True), 2)
                time.sleep(1)
            else:
                self.queue.get()
                break

            i += 1

            if i >= len(self.games):
                i = 0

    def update_with_error(self):
        while True:
            if self.queue.empty():
                self.lcd.text("Error", 1)
                self.lcd.text("Press button", 2)
                time.sleep(1)
            else:
                self.queue.get()
                break
