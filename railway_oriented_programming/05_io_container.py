from returns.io import IOFailure, IOResult, IOSuccess

def read_file(file_path: str) -> IOResult[str, Exception]:
    try:
        with open(file_path, "r") as file:
            return IOSuccess(file.read())
    except IOError as e:
        return IOFailure(e)
    

def process_data(data: str) -> str:
    return data.upper()


def main() -> None:
    file_io = read_file("user_data.txt")
    print(file_io)

    processed_data = file_io.map(process_data)
    processed_data.map(lambda data: print(data))
    print(processed_data)


if __name__ == '__main__':
    main()