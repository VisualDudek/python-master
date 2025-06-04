def write_warnings(log_entries: list[dict[str, str]]) -> None:
    def process_entry(entry: dict[str, str]) -> None:
        timestamped = f"{entry['timestamp']}: {entry['message']}\n"
        with open("warnings.log", "a") as f:
            f.write(timestamped + "\n")
            if "WARNING" in entry["message"]:
                print(f"Warning logged: {timestamped.strip()}")
        # file context manager will be opening and closing the file for each entry
        # ^^^ this is BAD

    list(map(process_entry, log_entries))
    # ^^^ need to use list() to force evaluation of the map !!!
    # BC map() returns a lazy iterator


def main() -> None:
    log_entries: list[dict[str, str]] = [
        {"timestamp": "2023-10-01 12:00:00", "message": "INFO: System started."},
        {"timestamp": "2023-10-01 12:05:00", "message": "WARNING: Low disk space."},
        {"timestamp": "2023-10-01 12:10:00", "message": "ERROR: Disk write failed."},
    ]

    write_warnings(log_entries)


if __name__ == "__main__":
    main()