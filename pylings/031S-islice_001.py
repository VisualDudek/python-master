"""
SOLUTION
Show me example of islice usage.
using: infinite built-in iterator
"""
from itertools import islice, count

for i in islice(count(), 5):
    print(i)
