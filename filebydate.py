#! /usr/bin/python3

# filebydate.py: sorts files based on ctime by separating into dated directories.

import os
from datetime import datetime

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

sort()
