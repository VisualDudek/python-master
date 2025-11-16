def main() -> None:
    words = ["code", "python", "ai", "refactor", "bug"]

    # Refactor this to use a dictionary comprehension
    length_dict: dict[str, int] = {}
    for word in words:
        if len(word) > 4:
            length_dict[word] = len(word)

    print(length_dict)


if __name__ == '__main__':
    main()