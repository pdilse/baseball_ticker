class Game:
    def __init__(self, info_dict):
        self.away_team = info_dict["away"]
        self.home_team = info_dict["home"]
        self.away_score = info_dict["away_score"]
        self.home_score = info_dict["home_score"]
        self.status = info_dict["status"]

    def has_game_started(self):
        return self.status.isdecimal() or self.status == "F"
