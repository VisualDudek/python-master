# Broken Code, this is nightmare to read
from typing import Any, Optional
from functools import reduce


def safe_get_nested_value(data: dict, keys: list[str], default: Any = None) -> Any:
    """Safely navigate nested dictionaries without exceptions."""
    return reduce(
        lambda d, key: d.get(key, {}) if isinstance(d, dict) else default,
        keys,
        data
    ) if data else default


def extract_d_value(item: dict[str, Any]) -> Optional[int]:
    """Extract the 'd' value from nested structure, returning None if not found."""
    if not item.get("flag", False):
        return None
    
    # Safe navigation through nested structure
    nested_value = safe_get_nested_value(item, ["a", "b", "c", "d"])
    return nested_value if isinstance(nested_value, int) else None


def calculate_transformed_value(d_value: Optional[int]) -> int:
    """Calculate the final transformed value based on extracted d_value."""
    return d_value + 5 if d_value is not None else -1


def transform_item(item: dict[str, Any]) -> int:
    """Transform a single item using declarative approach."""
    d_value = extract_d_value(item)
    return calculate_transformed_value(d_value)


def transform(data: list[dict[str, Any]]) -> list[int]:
    """Transform data using declarative functional approach."""
    return [transform_item(item) for item in data]


# Alternative: More concise functional version
def transform_functional(data: list[dict[str, Any]]) -> list[int]:
    """One-liner functional transformation."""
    return [
        (lambda d_val: d_val + 5 if d_val is not None else -1)(
            safe_get_nested_value(item, ["a", "b", "c", "d"]) 
            if item.get("flag", False) else None
        )
        for item in data
    ]


# Alternative: Using map for even more functional style
def transform_map_style(data: list[dict[str, Any]]) -> list[int]:
    """Transform using map for functional programming style."""
    return list(map(transform_item, data))


def main() -> None:
    data: list[dict[str, Any]] = [
        {"flag": True, "a": {"b": {"c": {"d": 1}}}},      
        {"flag": False, "a": {"b": {"c": {"d": 2}}}},
        {"flag": True, "a": {"b": {"c": {}}}},                   
        {"flag": True, "a": {"b": {}}},                          
        {"flag": True, "a": {}},                          
    ]
    
    print("Original data:")
    for i, item in enumerate(data):
        print(f"  {i}: {item}")
    
    print("\nTransformation results:")
    
    # Method 1: Declarative with helper functions (most readable)
    result1 = transform(data)
    print(f"Declarative approach: {result1}")
    
    # Method 2: Functional one-liner
    result2 = transform_functional(data)
    print(f"Functional approach:  {result2}")
    
    # Method 3: Map-based functional style
    result3 = transform_map_style(data)
    print(f"Map-based approach:   {result3}")
    
    # Verify all approaches give same result
    assert result1 == result2 == result3, "All approaches should give same result"
    print(f"\n✓ All approaches produce identical results: {result1}")
    
    # Show step-by-step breakdown for understanding
    print("\nStep-by-step breakdown:")
    for i, item in enumerate(data):
        d_value = extract_d_value(item)
        final_value = calculate_transformed_value(d_value)
        print(f"  Item {i}: flag={item.get('flag')}, d_value={d_value}, result={final_value}")


if __name__ == "__main__":
    main()