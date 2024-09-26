- use VS Code ext. "Mypy Type Checker" -> mypy 

## Topics:
- Duck Typing vs. Type Hints - collision between this two concepts
- inheritance is a solution but not ideal -> clear inheritance relationship BUT classes are tightly coupled
- Holy Grail -> Protocols, structural subtyping vs. nominal subtyping (inheritance)
- see problem in 005, structural subtyping is good but it can be better -> Protocols
- move from (inplicite interfance implementation) structural subtyping TO formal protocol
- ellipsis (...) syntax
- issues while using type hints with Protocols
- using type hints union is not an option
- `T = TypeVar("T", bound= )` syntax, in Python 3.12 type generic definition can be skiped in favor of `add[T: int | float]`
- mypy is not ready for above future syntax

Takeaway:
1. duck typing and type hints collide
2. Protocols are particularly useful when it’s impractical to modify the inheritance structure of classes. With protocols, you can focus on defining the desired behavior and characteristics without having to design complex inheritance relationships.
3. class that inherit form Protocol implements methods, which defines the protocol itself