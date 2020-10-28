# countdown.py
#
# Programmer   : Elad L
# Student no.  : 217
# Date         : 03/10/2020
#
# ---------------------------------------------------

# Imports
import argparse
import time

# Constants
parser = argparse.ArgumentParser()
parser.add_argument('-t', type=int,
                   help='Enter the number of seconds for the countdown')
args = parser.parse_args()


def countdown(n):
    while n > 0:
        print(n)
        n -= 1
        time.sleep(1)


def main():
    seconds = args.t
    countdown(seconds)
    

if __name__ == "__main__":
    main()
