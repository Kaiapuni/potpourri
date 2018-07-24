#! /usr/bin/python3

import os
from datetime import datetime

def date(filename):
    created = os.stat(filename).st_ctime
    readable = str(datetime.fromtimestamp(created))
    return readable[0: 10]

def existingDirectory(directoryName):
    return os.path.exists(directoryName) and os.path.isdir(directoryName)

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
