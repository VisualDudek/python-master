import ctypes

# Minimal example that shows PYTHONMALLOC=debug in action with ctypes

# Run with:
# PYTHONMALLOC=debug uv run 002_bad_ctypes.py

# Allocate a buffer for 10 bytes
buf = ctypes.create_string_buffer(10)

print("Writing within bounds...")
for i in range(10):
    buf[i] = b'a'

print("Attempting to write out of bounds...")
# This will catch the IndexError before the memory corruption occurs
for i in range(10, 15):
    buf[i] = b'b'  # Out of bounds write // NOPE -- this will raise an IndexError

print("Finished writing out of bounds.")