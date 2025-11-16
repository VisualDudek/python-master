def main() -> None:
    words = ["code", "python", "ai", "refactor", "bug"]

    # Refactor this to use a dictionary comprehension
    # SOLUTION
    # If condition is more complex I can put it in a function
    def is_long_word(word: str) -> bool:
        return len(word) > 4

    length_dict: dict[str, int] = {word: len(word) for word in words if is_long_word(word)}

    print(length_dict)


if __name__ == '__main__':
    main()