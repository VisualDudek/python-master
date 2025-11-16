import ctypes

# PYTHONMALLOC=debug catches memory corruption at the C level
# This example shows writing beyond allocated buffer bounds using ctypes

# Run with:
# PYTHONMALLOC=debug uv run 003_bad_ctypes.py

print("Creating a buffer of 10 bytes...")
buf = ctypes.create_string_buffer(10)

# This works fine - within bounds
print("Writing within bounds (0-9)...")
for i in range(10):
    buf[i] = ord('A')
print(f"Buffer content: {buf.raw}")

# Use ctypes pointer arithmetic to write beyond bounds
# This bypasses Python's IndexError check
print("\nAttempting memory corruption via pointer manipulation...")
ptr = ctypes.cast(buf, ctypes.POINTER(ctypes.c_char))

# Write beyond the allocated buffer - this causes memory corruption
# PYTHONMALLOC=debug will detect this when the memory is freed
for i in range(15):
    ptr[i] = b'X'

print("Finished writing. Deleting buffer to trigger debug check...")
del buf  # This will trigger PYTHONMALLOC=debug to check for corruption
print("If you see this, PYTHONMALLOC=debug didn't catch it (or isn't enabled)")