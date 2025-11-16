# print all files in this directory using pathlib

from pathlib import Path

def main() -> None:
    for file in Path('.').iterdir():
        if file.is_file():
            print(file.name)

if __name__ == '__main__':
    main()
    