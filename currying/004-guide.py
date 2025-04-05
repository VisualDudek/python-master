# type: ignore

# composition

from functools import wraps


def curry(func):
    @wraps(func)
    def curried(*args):
        if len(args) >= func.__code__.co_argcount:
            return func(*args)
        return lambda *more_args: curried(*args, *more_args)

    return curried


def compose(*funcs):
    def composed(data):
        for f in funcs:
            data = f(data)
        return data

    return composed


@curry
def strip_chars(chars, s):
    return s.strip(chars)


@curry
def strip_whitespace(s):
    return s.strip()


@curry
def to_case(case, s):
    return s.upper() if case == "upper" else s.lower()


@curry
def prefix(pre, s):
    return f"{pre}{s}"


@curry
def suffix(suf, s):
    return f"{s}{suf}"


clean_text = compose(
    strip_whitespace(),
    strip_chars("!?"),
    to_case("upper"),
    prefix("User: "),
    suffix("!"),
)

print(clean_text("   hello!?  "))  # Output: "User: HELLO!"
