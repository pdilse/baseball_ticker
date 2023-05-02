import time


class Ticker:
    gap_width = 3
    lcd_width = 16

    def __init__(self, queue, lcd):
        self.queue = queue
        self.lcd = lcd

    def display_loading(self, event):
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
        i = 0
        top_line = self.format_line(games, False)
        bottom_line = self.format_line(games, True)

        while True:
            if not self.queue.empty():
                self.queue.get()
                break

            self.lcd.text(top_line[i:i + self.lcd_width], 1)
            self.lcd.text(bottom_line[i:i + self.lcd_width], 2)

            if i % (self.lcd_width + self.gap_width) == 0:
                time.sleep(2)
            else:
                time.sleep(0.1)

            i += 1

            if i >= len(top_line) - self.lcd_width:
                i = 0

    def format_line(self, games, is_home):
        full_line = []

        for game in games:
            team = game.abbreviation(is_home)
            score = game.home_score if is_home else game.away_score
            game_line = f"{team}{(self.lcd_width - len(team) - len(score)) * ' '}{score}"
            full_line.append(game_line)

        full_line.append(full_line[0])

        return (' ' * self.gap_width).join(full_line)

    def update_with_error(self):
        while True:
            if self.queue.empty():
                self.lcd.text("Error", 1)
                self.lcd.text("Press button", 2)
                time.sleep(1)
            else:
                self.queue.get()
                break
