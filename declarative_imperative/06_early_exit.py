def scan_for_suspicious_activity(events: list[dict[str, str]]) -> None:
    for event in events:
        if is_suspicious(event):
            print(f"Suspicious activity detected: {event}")
            break


def is_suspicious(event: dict[str, str]) -> bool:
    return (
        "login" in event.get("type", "").lower()
        and "unusual" in event.get("details", "").lower()
    )


def main() -> None:
    events: list[dict[str, str]] = [
        {"type": "login", "details": "User logged in"},
        {"type": "login", "details": "Unusual login from new device"},
        {"type": "logout", "details": "User logged out"},
    ]

    scan_for_suspicious_activity(events)


if __name__ == "__main__":
    main()