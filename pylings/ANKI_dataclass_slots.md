| Front | Back |
|------|------|
| What is the fundamental design difference between `NamedTuple` and `dataclass`? | `NamedTuple` is immutable and tuple-based, optimized for fixed, read-only records, while `dataclass` is class-based and mutable by default, designed for structured objects with behavior. |
| Why can attributes of a `NamedTuple` not be changed? | Because `NamedTuple` subclasses `tuple`, and tuples are immutable; fields are stored positionally and cannot be reassigned after creation. |
| What is the idiomatic mutable replacement for `NamedTuple` in modern Python? | `@dataclass`, optionally with `slots=True` for memory efficiency. |
| Where are attributes stored in a plain `@dataclass` instance? | In the instance’s `__dict__`, which maps attribute names to values dynamically. |
| What does `slots=True` change in a `dataclass`? | It removes the per-instance `__dict__` and stores attributes in a fixed, slot-based layout defined at class creation time. |
| Why does `@dataclass(slots=True)` use less memory than a plain `dataclass`? | Because instances no longer allocate a `__dict__`, avoiding hash tables and storing attributes at fixed offsets. |
| What operation becomes impossible when using `slots=True`? | Adding new attributes dynamically (e.g. `obj.new_attr = ...`) raises `AttributeError`. |
| Why can attribute access be slightly faster with `slots=True`? | Attributes are accessed via fixed offsets instead of dictionary lookups. |
| How is `@dataclass(slots=True)` similar to `NamedTuple` but still different? | Both use fixed layouts and are memory-efficient, but `NamedTuple` is immutable and tuple-based, while `dataclass(slots=True)` is mutable and class-based. |
| If you replace a `NamedTuple` with `@dataclass(slots=True)`, what semantic change must you consciously accept? | Loss of immutability — fields can now be reassigned unless explicitly enforced. |
| Name one valid reason *not* to use `slots=True`. | When objects need dynamic attributes, heavy introspection, or compatibility with code relying on `__dict__`. |
| Complete the analogy: `NamedTuple` is to `tuple` as `dataclass(slots=True)` is to ______. | A mutable, structured record with fixed fields — effectively a “mutable NamedTuple”. |
