# Python Program to Get File Creation and Modification Date

import os.path, time
from pathlib import Path

file = Path('75.py')
print("Last modification time: %s" % time.ctime(os.path.getmtime(file)))
print("Last metadata change time or path creation time: %s" % time.ctime(os.path.getctime(file)))