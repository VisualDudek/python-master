# subclassing NamedTuple and adding methods

from typing import NamedTuple


class Point(NamedTuple):
    x: float
    y: float

    @property
    def distance_to_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5


# Usage
p = Point(3, 4)
print(p)  # Point(x=3, y=4)
print(p.distance_to_origin)  # 5.0 - note: no parentheses needed!


"""
Perfect! Here's why using `@property` is better in this case:

## Benefits of using `@property`:

1. **More intuitive API**: `p.distance_to_origin` reads like an attribute, which makes sense for a computed value
2. **Follows Python conventions**: Properties are the Pythonic way to expose computed attributes
3. **Cleaner syntax**: No need for parentheses when accessing the value
4. **Consistent with other attributes**: `p.x`, `p.y`, and `p.distance_to_origin` all use the same syntax
5. **Future flexibility**: If you later need to cache the result or add validation, you can do so without changing the API

## When to use methods vs properties:

- **Use `@property`** when:
  - Computing a derived value (like distance)
  - No parameters needed
  - Represents a "state" or "attribute" of the object
  - Fast computation (no heavy I/O or long calculations)

- **Use methods** when:
  - Taking parameters
  - Performing actions (like `save()`, `delete()`)
  - Expensive operations that should be explicit
  - Side effects are involved

Your intuition was spot on! The property approach is much more elegant for this use case.
"""