class Game:
    def __init__(self, a_team, h_team, a_score, h_score):
        self.away_team = a_team
        self.home_team = h_team
        self.away_score = a_score
        self.home_score = h_score

    def abbreviation(self, is_home):
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
            "San Diego Padres": "SD",
            "San Francisco Giants": "SF",
            "Seattle Mariners": "SEA",
            "St. Louis Cardinals": "STL",
            "Tampa Bay Rays": "TB",
            "Texas Rangers": "TEX",
            "Toronto Blue Jays": "TOR",
            "Washington Nationals": "WAS"
        }

        full_name = self.home_team if is_home else self.away_team
        return teams[full_name]
