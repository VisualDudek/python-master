def main() -> None:
    words = ["code", "python", "ai", "refactor", "bug"]

    # Refactor this to use a dictionary comprehension
    # SOLUTION
    length_dict: dict[str, int] = {word: len(word) for word in words if len(word) > 4}

    print(length_dict)


if __name__ == '__main__':
    main()