#! /usr/bin/python3

import os
from datetime import datetime

created = os.stat('mickeydir.py').st_ctime

print(datetime.fromtimestamp(created))
readable = str(datetime.fromtimestamp(created))
print(readable[0: 10])
