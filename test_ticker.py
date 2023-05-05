import pytest
from ticker import Ticker
from game import Game

@pytest.fixture
def ticker():
    return Ticker(0, 0)


@pytest.fixture
def games():
    games = [
        Game("Chicago Cubs", "Miami Marlins", "10", "2"),
        Game("Houston Astros", "Texas Rangers", "4", "0"),
        Game("Colorado Rockies", "San Diego Padres", "2", "6")
    ]

    return games


def test_line_lengths_equal(ticker, games):
    away_line = ticker.format_line(games, False)
    home_line = ticker.format_line(games, True)
    assert len(away_line) == len(home_line)


def test_line_length(ticker, games):
    lcd_width = 16
    gap_width = 3
    home_line = ticker.format_line(games, True)
    assert len(home_line) == (len(games) + 1) * lcd_width + len(games) * gap_width
