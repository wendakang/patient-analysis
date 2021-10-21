"""
This module counts the number of line in standard input
"""

import sys

count = 0
for lines in sys.stdin:
    count += 1

print(count, 'lines in standard input')
