#! /usr/bin/python3

# filebydate.py: sorts files based on ctime by separating into dated directories.

import os
from datetime import datetime

import argparse

# Create argument parser
def filebydateparser():
    parser = argparse.ArgumentParser(description = "Sort the contents of the working directory into separate folders by date.")

    parser.add_argument("-p", "--path", help = "Path to target directory, when not current working directory")
    parser.add_argument("--hidden", action = "store_true", help = "Include hidden files when sorting")
    parser.add_argument("-l", "--long", action = "store_true", help = "Use full date and time")
    parser.add_argument("-t", "--time", action = "store_true", help = "Disregard date and sort only by time")
    parser.add_argument("-o", "--only", action = "store_true", help = "Only use specified resolutions of time")
    parser.add_argument("-n", "--name", action = "store_true," help = "Use month names instead of numbers")

    timeResolution = parser.add_argument_group()
    timeResolution.add_argument("-s", "--second", action = "store_true", help = "Sort down to the second")
    timeResolution.add_argument("-m", "--minute", action = "store_true", help = "Sort down to the minute")
    timeResolution.add_argument("-h", "--hour", action = "store_true", help = "Sort down to the hour")

    dateResolution = parser.add_argument_group()
    dateResolution.add_argument("-d", "--day", action = "store_true", help = "Sort down to the day")
    dateResolution.add_argument("-m", "--month", action = "store_true", help = "Sort down to the month")
    dateResolution.add_argument("-y", "--year", action = "store_true", help = "Sort down to the year")

    args = parser.parse_args()
    return args

# date returns the calendar date portion of a file's timestamp.
def date(filename):
    created = os.stat(filename).st_ctime #pull ctime data from file
    readable = str(datetime.fromtimestamp(created)) #convert to human-readable format
    return readable[0: 10] #shorten from date and time to just date

# existingDirectory checks if a directory of a given name exists.
def existingDirectory(directoryName):
    return os.path.exists(directoryName) and os.path.isdir(directoryName)

# sort iterates through a directory's files and checks their ctime against the names of the subdirectories within. If a match exists, the file is placed within the existing directory. If not, it is placed within a newly-created directory named after the corresponding date.
def sort():
    directory = os.fsencode(os.getcwd())
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if os.path.isdir(filename):
            continue
        datename = date(filename)
        if existingDirectory(datename):
            os.rename(os.getcwd() + "/" + filename, os.getcwd() + "/" + datename + "/" + filename)
        else:
            os.makedirs(datename)
            os.rename(os.getcwd() + "/" + filename, os.getcwd() + "/" + datename + "/" + filename)

def main():
    sort()

if __name__ = "__main__":
    args = filebydateparser()
    main()
