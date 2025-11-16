# Run with:
# PYTHONMALLOCSTATS=1 uv run 004_malloc_stats.py
# will print statistics of pymalloc allocator every time a new
# pymalloc object arena is created and on shutdown.


def allocate_memory():
    # Create various data structures to trigger memory allocations
    large_list = [i for i in range(10)]
    

if __name__ == "__main__":
    allocate_memory()
    print("\nProgram finishing - memory stats will be printed now...")