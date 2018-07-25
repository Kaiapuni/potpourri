#! /usr/bin/python3

# readtime.py: a script which prints the ctime of a file in human-readable format.
# ctime is not necessarily the creation date, but it's the closest linux has.

import os
from datetime import datetime

# Pull the ctime of the file
created = os.stat('filebydate.py').st_ctime

# Print the creation date in human-readable format
print(datetime.fromtimestamp(created))
