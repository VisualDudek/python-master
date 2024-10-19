**Takeaway:**
1. Abstract base classes (ABCs) complement duck-typing, see POC 005-6
2. ABCs is based on nominal typing
3. Protocols as alternative to ABCs -> first ABCs next Protocols
4. ABCs conceptually belongs to subclasses and OOP hierarhy, whereas protocols belongs more closely to the places where they're used.
5. Interface segregation, it is part of SOLID
6. ABCs in Python provide a mechanism for defining interfaces. An interface defines a set of methods that a class must implement to be considered compatible with the interface.
7. problems with define interface by `hasattr()`

**Key Topics:**

PEP 3119 - Introducing Abstract Base Classes

**Abstract base classes (ABCs)** complement duck-typing by providing a way to define interfaces when other techniques like `hasattr()` would be clumsy or subtly wrong (for example with magic methods). ABCs introduce virtual subclasses, which are classes that don’t inherit from a class but are still recognized by isinstance() and issubclass(); see the abc module documentation. Python comes with many built-in ABCs for data structures (in the collections.abc module), numbers (in the numbers module), streams (in the io module), import finders and loaders (in the importlib.abc module). You can create your own ABCs with the abc module.

**duck-typing** A programming style which does not look at an object’s type to determine if it has the right interface; instead, the method or attribute is simply called or used (“If it looks like a duck and quacks like a duck, it must be a duck.”) By emphasizing interfaces rather than specific types, well-designed code improves its flexibility by allowing polymorphic substitution. **holy grail of understanding** -> Duck-typing avoids tests using `type()` or `isinstance()`. (Note, however, that duck-typing can be complemented with abstract base classes.) Instead, it typically employs `hasattr()` tests or EAFP programming.

**EAFP** Easier to ask for forgiveness than permission. This common Python coding style assumes the existence of valid keys or attributes and catches exceptions if the assumption proves false. This clean and fast style is characterized by the presence of many `try` and `except` statements. The technique contrasts with the LBYL style common to many other languages such as C.

**LBYL** Look before you leap. This coding style explicitly tests for pre-conditions before making calls or lookups. This style contrasts with the EAFP approach and is characterized by the presence of many `if` statements. 


**in deep** why using `hasattr()` to check for magic methods can become cumbersome or lead to subtle errors in Python?
- Only check existence, not correctness, -> e.g. `__len__()` must return a non-negative integer, `__iter__()` must return an iterator. Simply using `hasattr()` won't tell you whether these requirements are met.
- Performance overhead with multiple checks, -> e.g. to implement the iterable protocol, a class should implement both `__iter__()` and `__next__()`, if you use `hasattr()` to manually check for all necesssary methods, it can become tedious and repetitive. If more methods are required (e.g. `__getitem__`, `__len__`) this quickly becomes unmanageable. Relying on `hasattr()` for each individual check is not scalable or elegant.
- Different lookup mechanism: Magic methods are looked up on the class (type) of an object, not on the instance itself. This means that even if an instance doesn't have `__len__` in its `__dict__`, it might still respond to `len()` because the method exists in its class. If `__len__` is defined in a metaclass or added dynamically, `hasattr()` might not detect it correctly.
- Magic methods can be provided via descriptors or metaclasses, -> altering their availablility in ways that `hasattr()` might not correctly detect, see example below:
```python
class MyClass:
    def __getattr__(self, name):
        if name == '__len__':
            return lambda: 10

obj = MyClass()
print(len(obj))          # Outputs: 10
print(hasattr(obj, '__len__'))  # Outputs: False
```
- False Positives, -> An object might have an attribute with the same name as a magic method, but not actually conform to the expected protocol. See example: `hasattr()` returns `True`, but attempting to iterate over the object fails.
```python
class NotIterable:
    __iter__ = None  # Has __iter__ attribute but is not callable

obj = NotIterable()
print(hasattr(obj, '__iter__'))  # Outputs: True
for item in obj:
    pass  # Raises TypeError: 'NoneType' object is not callable
```

**in deep** understanding Virtual Subclass.
- Why use virtual subclasses? -> Virtual subclasses give you the flexibility to declare that a class should be considered part of an interface without enforcing inheritance. This is useful in cases where you don't want to change an existing class’s inheritance chain but still want to declare that it adheres to a particular interface or contract.
- holy grail of understanding, -> in Python, virtual subclasses are classes that are recognized by `isinstance()` and `issubclass()` checks as being a subclass of an abstract base class (ABC), even if they don’t explicitly inherit from that ABC. This is different from a regular subclass, which directly inherits from a parent class. Virtual subclasses are registered with the ABC using the `register()` method, rather than using normal class inheritance. Once registered, a virtual subclass will behave as if it were a subclass of the ABC for the purposes of `isinstance()` and `issubclass()`, but it doesn’t actually inherit any methods or attributes from the ABC.
- Why you want class that doesn't inherit from parent? show me the real POC

**in deep** interface vs. contracts
- An interface in programming refers to a defined structure that specifies a set of methods and properties that a class must implement. It represents the "what" an object can do, without providing the implementation details of "how" it does it.
- holy grail of understanding, -> A contract in programming is a broader concept that not only specifies what methods or properties an object should provide (like an interface) but also adds constraints or guarantees about how these methods should behave. In other words, a contract focuses on both the structure and the behavior. Enforce preconditions and postconditions.

**in deep** Built-in ABCs:
Python comes with many built-in ABCs across several modules, each catering to specific use cases:
- Data Structures: The `collections.abc` module provides ABCs for common data structures like `Iterable`, `Sequence`, `Mapping`, and `Set`. These define standard behaviors for collections, ensuring that any class implementing one of these ABCs has the required methods (like `__len__()`, `__getitem__()`, etc.).
- Numbers: The numbers module defines ABCs for numeric types, such as `Number`, `Integral`, and `Complex`. This ensures that any numeric class meets the expected behaviors for arithmetic operations.
- Streams: The io module includes ABCs for working with streams (e.g., `IOBase`, `TextIOBase`, `BufferedIOBase`). These base classes ensure that any object representing input/output streams adheres to the expected interface.
- Import Finders and Loaders: The `importlib.abc` module provides ABCs for Python’s import system, defining the interfaces for custom import finders and loaders.