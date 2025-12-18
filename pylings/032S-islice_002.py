"""
SOLUTION
Show me example of islice usage.
using: generator comprehension, explain why
"""
from itertools import islice

gen = (x * x for x in range(10_000)) # lazy evaluation, saves memory

# first_five = list(gen)[:5]  # BAD: would generate all 10,000 items first

for i in islice(gen, 5):
    print(i)
