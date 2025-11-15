import psutil, os

# In theory the memory used by the Python process should not shrink
# after deleting a large list, due to how pymalloc works.
# BUT this test produces different results.

def show():
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / (1024 ** 2)
    print(f"Memory Usage: {mem:.2f} MB")

data = [x for x in range(10**7)]
show()
del data
show()