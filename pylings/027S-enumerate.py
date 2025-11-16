def main() -> None:
    words = ["code", "python", "ai", "refactor", "bug"]

    # Refactor this to use enumerate
    # SOLUTION
    for i, word in enumerate(words):
        print(f"{i}: {word}")


if __name__ == '__main__':
    main()