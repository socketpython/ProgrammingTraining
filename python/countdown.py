import argparse
import time


parser = argparse.ArgumentParser()
parser.add_argument('-t', type=int,
                   help='Enter the number of seconds for the countdown')
args = parser.parse_args()


def countdown(n):
    while n > 0:
        print(n)
        n -= 1
        time.sleep(1)


seconds = args.t
countdown(seconds)
