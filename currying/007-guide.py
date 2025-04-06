# type: ignore

# Inspecting Closure Vars in lambda

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


closure_fn = strip_chars("abc")

# Inspecting closure variables
if closure_fn.__closure__:
    closure_vars = {
        name: cell.cell_contents
        for name, cell in zip(closure_fn.__code__.co_freevars, closure_fn.__closure__)
    }
    print("Closure Variables:", closure_vars)
else:
    print("No closure variables.")

closure_fn = closure_vars["curried"]
if closure_fn.__closure__:
    closure_vars = {
        name: cell.cell_contents
        for name, cell in zip(closure_fn.__code__.co_freevars, closure_fn.__closure__)
    }
    print("Closure Variables for lmbda fn. ???:", closure_vars)
else:
    print("No closure variables.")


# closure_fn.__code__.co_freevars provides the names of the closed-over
# variables
