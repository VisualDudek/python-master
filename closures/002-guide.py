# Maintaining State With Closures


def make_counter():
    count = 0  # Initial state in the outer function's scope

    def counter():
        nonlocal count  # Declare count as non-local to modify it
        count += 1  # Increment the captured state
        return count

    return counter  # Return the inner function (closure)


# Usage:
counter_a = make_counter()
print(counter_a())  # Output: 1
print(counter_a())  # Output: 2

counter_b = make_counter()
print(counter_b())  # Output: 1
