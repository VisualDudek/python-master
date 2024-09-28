import itertools

# itertools.cycle(iterable)
# repeats indefinitely
cycler = itertools.cycle(["a", "b", "c"])
values = [next(cycler) for _ in range(6)]
assert values == ["a", "b", "c", "a", "b", "c"]

# Roud-Robin Scheduler: Implement a round-robin scheduler that cycles
# through a list of tasks or participants

# Infinite Progress Indicator:
import time


def progress_indicator():
    spinner = itertools.cycle(["|", "/", "-", "\\"])
    while True:
        print(next(spinner), end="\r")
        time.sleep(0.2)


# Uncomment the following line to see the progress indicator in action
progress_indicator()
