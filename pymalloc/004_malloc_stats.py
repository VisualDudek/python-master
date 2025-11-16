# Run with:
# PYTHONMALLOCSTATS=1 uv run 004_malloc_stats.py

def allocate_memory():
    # Create various data structures to trigger memory allocations
    large_list = [i for i in range(10)]
    
    # Create some strings
    # strings = [f"string_{i}" * 10 for i in range(10000)]
    
    # Nested structures
    # nested = [[j for j in range(100)] for i in range(1000)]
    

if __name__ == "__main__":
    allocate_memory()
    print("\nProgram finishing - memory stats will be printed now...")