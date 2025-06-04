from returns.result import safe


@safe
def divide(a: int, b: int) -> int:
    return a // b


def main() -> None:
    safe_result = divide(10, 2)
    error_result = divide(10, 0)

    print(safe_result, error_result, sep='\n')

    print(divide(10, 0).value_or(-1))


if __name__ == "__main__":
    main()