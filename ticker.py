import time

class Ticker:
    def __init__(self, queue, lcd):
        self.games = []
        self.queue = queue
        self.lcd = lcd

    def display_loading(self):
        self.games = []
        # display loading text

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
