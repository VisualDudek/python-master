# Structural Pattern Matching


leads to more elegant, concise, and readable code writtern in a **declarative** style.

resemblance to siwtch statement in C-family languages is **deceptive**. The classic switch statement controls the execution flow based on the exact value stored in a variable. It effectively works as a chained sequence of mutually exclusive if..elif... equality comparisons, but with a more succinct and readable syntax.

Each pattern describes the structure of an object to match, including its type, shape, value, and identity. It can also specify the individual pieces of which an object is made.


## Takeaway

- selective data extraction from complex data structures.
- pattern is not your typical expression, subject is (002)
- structural pattern is similar to tuple unpacking or left side of assignment (003)
- you can nest match statements
- basic syntax understanding: match statement (subject) and case clauses (structural pattern)
- avoid using pattern mataching as `switch` statement replacement, use **jump table** (004)
- match statement, better to bind subject to variable using warlus operator
- body of the match statement can only conisist of a non-empty sequence of case clauses
- there are different kind of structural pattern in case clauses (1) literal pattern (2) capture pattern ...
- can combine subpatterns into union, use vertical bar `|`
- when you dealing with overlapping patterns -> order of case clauses will matter
- `exec()` vs. `eval()`
- expressions are statements, but not the other way around -> in overlapping patterns expression should go first. Statement in this context is more generic -> expression is a statement wiht side effect
- Literal type checking 
- Unlike many other programming languages, Python allows the case clauses in pttern matching to remain **non-exhaustive**
- catch-all case by using wildcard pattern (_) **behaves linke keyword** within a structural pattern -> never binds the subject to a name, so you won't be able to refer to it inside case clause.
- you can reuse the underscore several times as a subpattern to discard certain elements of other patterns.
- **Literal Pattern** generally lets you restrict the value of the subject instead of its type or structure -> suitable for emulating the `switch` statement BUT do not do this
- f-string do not work with structural pattern bc. f-stirng typically involve string interpolation, which must be done at runtime. -> f-strings are NOT Literal patterns
- ensure strict type checking using class pattern
- **Value Pattern** let you recognize variables that should be treated as constans, typically belong to some namespace, such as a class, enum or a Ptyhon module, which you can access with the dot operator. (015, 016)
- Capture pattern defines its own local variable, which means that the captured name will continiue to live outside your match block
- (!) plain capture pattern will make the subsequent case clauses unreachable bc. it matches the subject unconditionally
- Capture patterns are the cornerstone of **destructuting**. You'll often use them as subpatterns to extract piece of information from complex objects that you want to decompose. (018)
- you can parse iterable using **Sequence Pattern** (019)
- to catch empyt sequence use empty brackets `[]` or `()` (019)
- **Sequence Pattern** do support only smal subset of Python sequences: `tuple()` `list()` `range()` `memoryview()` `array.array()` `collections.deque()` `collections.nametuple()` user-defined derivatives of `Sequence` and `MutableSequence` abc.
- Sequence pattern will match objects that you built with a list comprehension.
- Sequence pattern DO NOT SUPPORT: `str()` `bytes()` and `bytearray()`
- use start operator to match sequence of lenght two or more. (020)
- you can impose additional restriction on the sequence type using class pattern (021)
- **Mapping Pattern**, dictionaries are among one of the most important data types (022)
- BC mappings are unordered collections of key-value, it doesn't matttern how you arrange your key-value pairs in pattern (022)
- Values in a mapping pattern can be almost anything BUT the corresponding keys must be either literal patterns or value patterns. CANNOT use capture patterns
- Mapping pattern besides `dict` will match also: `collections.` `ChainMap` `Counter` `OrderedDict` `UserDict` `defaultdict`
- when you use an empty dict literal `{}` then pattern will match just about any mapping (023)
- **Mapping Pattern** vs. **Sequence Pattern**, sequence patterns require you to either list all expected items or use the star operator (*) to indicate a variable-length sequence. In contrast, mapping patterns ignore any extra keys that exist in the subject but that you didn’t explicitly include in your pattern.
- in mapping pattern you can use `**` (standard dict unpacking) to capture multiple key-value pairs into smaller dict (024)
- (???) to avoid side effects as much as possible, Python doesn't use the squre brackets syntax when matching subject to one of your mappings pattarns. Rather than calling `.__getitem__()`,which square brackets use under the hood, it invodes `.get()` on the subject.
- instead of explicit calling `isinstance()` on the subject, you can check if the subject is an instance of the given type by using a class pattern. (025) **mind bending**
- you can use kwargs of the class constructor to extract attribute values, positional args are not supported out of the box, class pattern needs to specify attributes order using `.__match_args__` (026)
- fields not automatically init. in a data class are excluded form pattern matching (e.g. `__post_init__`)
- **mind bending** Structual Pattern Matching works well also with **structural subtypes** (not only with nominal subtypes). (027)
- since class pattern call the `isinstance()` on the subject, make sure that the any protocol you match against was decorated with `@runtime_checkable`. (027)

## Learning Curve
`AliasTypes` cannot be directly used as class patterns
```python
from typing import TypeAlias

Number: TypeAlias = int | float

...
 case list([Number() as x, Number() as y, 0]) # wont work

 # I am afraid you need this:
 case list([int() | float() as x, ...])
```

`@dataclass` decorator does not directly support class variables.
Class variables are defined using the `ClassVar` type hint from `typing` module. (pylings 011)

`Tuple[int, ...]` vs. `List[int]` (021)

You can quickly convert dataclass into dict `from dataclasses import asdict` (022)

Clean and nice way to test/introduce many types based on dict input. (023)

When you want to annotate variable and expression in `for loop` you cannot do this in `for-loop` expresion, and do not try only annotate variable, JUST annotate before `for-loop` expresion (!!!) (025)

type annotation for structural subtypes is crazy (027)


## Whent to use structural pattern matching?
The answer to when to use pattern matching is right there in its name: structural pattern matching. In short, you should use pattern matching when you want to **make a decision based on the structure of complex data and possibly destructure it at the same time**. This approach can help you adopt a more declarative coding style, which is especially beneficial if you’re following the functional programming paradigm.

In contrast, if you’re making a decision **based on complex business rules** that require a lot of computation, especially if the conditions are non-exclusive or incremental, then you may be better off choosing a different language construct. There are some well-established and usually more appropriate idioms in Python for such scenarios, like a chain of if...elif... statements.

### GPT help
- What are common use case of structural pattern matching in Python?
- Provide examples of python frameworks or libraries that use structural pattern matching

## Key Topics

**Soft Keywords** in Python 3.10 and later, my understanding: it is only for backward compatibility

**match statement** - subject

**case clauses** - structural pattern
1. **Literal Pattern**
2. **Class Pattern** for strict type checking  
3. **Value pattern**
4. **Capture pattern** - resembles the typical variable declaration
5. **Wildcard pattern**
6. **Sequence Pattern** - can quickly recognize a sequence pattern by the presence of square brackets
7. **Mapping Pattern**

**guards**

**`TypeAlias`**

## mypy -> pyright
```python
# pyright: reportMatchNotExhaustive=false
```

```python
# type: ignore[override]
```