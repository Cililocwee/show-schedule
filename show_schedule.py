# as of now, this is the most up to date version of this program 2/18/2015
# this program is designed to simply inform me of the day and what sets of media I need to access

import datetime
import time


def main():
    today = datetime.datetime.today().weekday()
    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

    media = {'Monday': {'shows': ['Family Guy', 'American Dad'], 'manga': []},
             'Tuesday': {'shows': [], 'manga': []},
             'Wednesday': {'shows': ['Supernatural', 'The Flash'], 'manga': []},
             'Thursday': {'shows': ['South Park', 'Law and Order: SVU'], 'manga': []},
             'Friday': {'shows': [], 'manga': ['Bleach']},
             'Saturday': {'shows': ['Sword Art Online', 'World Trigger'], 'manga': []},
             'Sunday': {'shows': [], 'manga': ['Fairy Tail']}
             }

    def shows_time(wDay):
        print("Today is %s!" % days[wDay])
        time.sleep(.5)

        if len(media[days[wDay]]['shows']) > 0:
            print("   You should download:")
            for x in media[days[wDay]]['shows']:
                time.sleep(.4)
                print('\t*' + x)
            time.sleep(.4)

        if len(media[days[wDay]]['manga']) > 0:
            print("   You should read:")
            for x in media[days[wDay]]['manga']:
                time.sleep(.4)
                print('\t*' + x)
            time.sleep(.4)

    shows_time(today)
    input()


if __name__ == "__main__":
    main()
