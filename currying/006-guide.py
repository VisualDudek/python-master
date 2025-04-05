# type: ignore

# chaining with >> operator (synctactic sugar)

from functools import wraps


def curry(func):
    @wraps(func)
    def curried(*args):
        if len(args) >= func.__code__.co_argcount:
            return func(*args)
        return lambda *more_args: curried(*args, *more_args)

    return curried


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


class Pipeable:
    def __init__(self, func):
        self.func = func

    def __rrshift__(self, other):
        return self.func(other)


# Wrap our curried functions
strip_white = Pipeable(strip_whitespace())
strip = Pipeable(strip_chars("!? "))
case = Pipeable(to_case("upper"))
pre = Pipeable(prefix("User: "))
suf = Pipeable(suffix("!"))

# Now you can write:
result = "   hello!?  " >> strip_white >> strip >> case >> pre >> suf
print(result)  # Output: "User: HELLO!"

"""
" hello " >> strip_white
" hello ".__rshift__(strip_white) # zwraca NotImplemented więc sprawdza fallback
strip_white.__rrshift__(" hello ") # co oznacza:
stip_whitespace(" hello ") # czyli
" hello ".strip() # returns: "hello"
"""
