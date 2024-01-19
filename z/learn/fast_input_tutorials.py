# Reference - https://codeforces.com/blog/entry/63102

import os
import sys
from atexit import register
from io import BytesIO

sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))
input = BytesIO(os.read(0, os.fstat(0).st_size)).readline
