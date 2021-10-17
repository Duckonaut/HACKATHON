from datetime import datetime
from time import sleep
import webbrowser


def main():
    while datetime.now().strftime("%H:%M") != "21:37":
        sleep(1)

    webbrowser.open('https://www.youtube.com/watch?v=0qzLRlQFFQ4&ab_channel=VerbumDei', new=2)


if __name__ == "__main__":
    main()
