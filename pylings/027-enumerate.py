def main() -> None:
    words = ["code", "python", "ai", "refactor", "bug"]

    # Refactor this to use enumerate
    for i in range(len(words)):
        print(f"{i}: {words[i]}")


if __name__ == '__main__':
    main()