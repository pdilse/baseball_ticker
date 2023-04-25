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

            if i < 3:
                i += 1
            else:
                i = 1

            time.sleep(0.5)

            if event.is_set():
                self.lcd.text("", 1)
                return

    def update_with_games(self, games):
        self.games = games
        i = 0

        while True:
            if self.queue.empty():
                self.lcd.text(str(i), 1)
                time.sleep(1)
                i += 1
            else:
                self.queue.get()
                break

    def update_with_error(self):
        pass
