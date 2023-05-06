# baseball_ticker
Small Raspberry Pi project simulating a scrolling ticker for recent baseball scores. Data is scraped from Baseball Reference with Beautiful Soup. Teams and scores are then formatted into two long strings for output to the LCD screen. The games will continually scroll horizontally, briefly stopping at each game. Pressing the button will reload the data, either to update the games or because of a loading error.

Python features used:
  - Requests and Beautiful Soup modules to load game data
  - Threads (to detect button press and for loading animation)
  - Queues for inter-thread communication
  - Exception handling
  - Pytest


![IMG_2791](https://user-images.githubusercontent.com/105980062/236580063-4999bfa0-254b-4254-b7a4-45128917c6b5.jpeg)
Game score.

![IMG_2792](https://user-images.githubusercontent.com/105980062/236580778-2d48137f-8f52-4396-8d58-ca8bc6e6d117.jpeg)
Scrolling horizontally to the next game.
