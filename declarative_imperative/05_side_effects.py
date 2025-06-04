def write_warnings(log_entries: list[dict[str, str]]) -> None:
    with open("warnings.log", "a") as f:
        for entry in log_entries:
            timestamped = f"{entry['timestamp']}: {entry['message']}\n"
            f.write(timestamped + "\n")
            if "WARNING" in entry["message"]:
                print(f"Warning logged: {timestamped.strip()}")


def main() -> None:
    log_entries: list[dict[str, str]] = [
        {"timestamp": "2023-10-01 12:00:00", "message": "INFO: System started."},
        {"timestamp": "2023-10-01 12:05:00", "message": "WARNING: Low disk space."},
        {"timestamp": "2023-10-01 12:10:00", "message": "ERROR: Disk write failed."},
    ]

    write_warnings(log_entries)


if __name__ == "__main__":
    main()