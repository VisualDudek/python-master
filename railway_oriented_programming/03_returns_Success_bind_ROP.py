from returns.result import Failure, Result, Success


def parse_number(string: str) -> Result[int, str]:
    try:
        return Success(int(string))
    except ValueError:
        return Failure("Invalid number format")
    

def add_ten(number: int) -> Result[int, str]:
    return Success(number + 10)


def main():
    result = parse_number("10").bind(add_ten)
    error_result = parse_number("NaN").bind(add_ten)

    print(result)
    print(error_result)


if __name__ == "__main__":
    main()