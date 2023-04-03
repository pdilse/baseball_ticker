import requests
from bs4 import BeautifulSoup


def main():
    url = "https://www.baseball-reference.com/boxes/"

    try:
        response = requests.get(url)
        print(response.text)
    except requests.exceptions.ConnectionError:
        print("connection error")


if __name__ == '__main__':
    main()
