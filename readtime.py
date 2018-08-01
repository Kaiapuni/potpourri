#! /usr/bin/python3

# readtime.py: a script which prints the ctime of a file in human-readable format.
# ctime is not necessarily the creation date, but it's the closest linux has.

import os
from datetime import datetime

import argparse

# Create argument parser
def dateparser():
    parser = argparse.ArgumentParser(description = 'Read the ctime of a file in human-readable format.')

    parser.add_argument("filename", help = "Name of file to read date")
    parser.add_argument("-l", "--long", action = "store_true", help = "Print full date and time")

    args = parser.parse_args()
    return args

# Convert ctime
def timetranslate(filename):

    # Pull the ctime of the file
    created = os.stat(filename).st_ctime

    # Return the creation date in human-readable format
    return datetime.fromtimestamp(created)

def main(arguments):
    cdatetime = timetranslate(arguments.filename)
    if arguments.long:
        return(str(cdatetime))
    else:
        return(str(cdatetime)[0:10])

if __name__ == "__main__":
    args = dateparser()
    print(main(args))
