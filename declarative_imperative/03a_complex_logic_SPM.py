from typing import Any

def transform(data: list[dict[str, Any]]) -> list[int]:
    result: list[int] = []
    
    for item in data:
        match item:
            # Pattern: flag is True and nested structure exists with 'd' value
            case {"flag": True, "a": {"b": {"c": {"d": d_value}}}}:
                result.append(d_value + 5)
            # Pattern: flag is True and nested structure exists but 'd' is missing (default to 0)
            case {"flag": True, "a": {"b": _ }}:
                result.append(0 + 5)  # default value 0 + 5
            # Pattern: flag is True but structure is incomplete - append -1
            case {"flag": True}:
                result.append(-1)
            # Pattern: flag is False or any other case - append -1
            case _:
                result.append(-1)
    
    return result


def main() -> None:
    data: list[dict[str, Any]] = [
        {"flag": True, "a": {"b": {"c": {"d": 1}}}},      
        {"flag": False, "a": {"b": {"c": {"d": 2}}}},
        {"flag": True, "a": {"b": {"c": {}}}},                   
        {"flag": True, "a": {"b": {}}},                          
        {"flag": True, "a": {}},                          
    ]
    
    transformed_data = transform(data)
    print("Transformed data:", transformed_data)


if __name__ == "__main__":
    main()