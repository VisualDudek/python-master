# Currying


Currying is a functional programming concept where a function with multiple arguments is transformed into a sequence of functions, each taking **one argument at time**.

- transformacja przy uzyciu konceptu Closures
- Python nie ma automatycznego currying-u, jedynie `functools.partial`
- custom `curry` decorator that transforms a multi-argument function into a curried version, ADVANCED 


**VERY ADVANCED** Example:
Celem jest możliwość następującego pipelinu:
```python
pipeline = strip_chars("!?") >> to_case("upper") >> prefix("User: ") >> suffix("!")

print(clean_text("  hello!?   ")) # Output: "User: HELLO!"
```
- opcja 1: `004-guide.py` composition
- opcja 2: `pipe()` helper that lets you chain fn calls like Unix shell
- opcja 3: `>>` operator, syntactic sugar `006-guide.py`; ojojoj `__rshift__` and fallback `__rrshift__`

How `__rrshift__` works:
When executing an operation like:
```python
result = x >> y
```
Python performs the following steps:

1. First, it checks if the left-hand object (x) defines an __rshift__ method:
```python
x.__rshift__(y)
```
2. If x.__rshift__(y) returns NotImplemented or is not defined, Python checks if the right-hand object (y) defines the reflected method __rrshift__:
```python
y.__rrshift__(x)
```
3. If y also returns NotImplemented or doesn't define __rrshift__, Python raises a TypeError.
