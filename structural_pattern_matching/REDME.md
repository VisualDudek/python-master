# Structural Pattern Matching


leads to more elegant, concise, and readable code writtern in a **declarative** style.

resemblance to siwtch statement in C-family languages is **deceptive**. The classic switch statement controls the execution flow based on the exact value stored in a variable. It effectively works as a chained sequence of mutually exclusive if..elif... equality comparisons, but with a more succinct and readable syntax.

Each pattern describes the structure of an object to match, including its type, shape, value, and identity. It can also specify the individual pieces of which an object is made.


## Takeaway

- selective data extraction from complex data structures.
- pattern is not your typical expression
- structural pattern is similar to tuple unpacking or left side of assignment
- you can nest match statements
- basic syntax understanding: match statement (subject) and case clauses (structural pattern)
- match statement, better to bind subject to variable using warlus operator
- body of the match statement can only conisist of a non-empty sequence of case clauses
- there are different kind of structural pattern in case clauses (1) literal pattern (2) capture pattern
- can combine subpatterns into union, use vertical bar `|`
- when you dealing with overlapping patterns -> order of case clauses will matter
- `exec()` vs. `eval()`
- expressions are statements, but not the other way around -> in overlapping patterns expression should go first. Statement in this context is more generic -> expression is a statement wiht side effect
- Literal
- Unlike many oteer programming languages, Python allows the case clauses in pttern matching to remain **non-exhaustive**

## Whent to use structural pattern matching?
The answer to when to use pattern matching is right there in its name: structural pattern matching. In short, you should use pattern matching when you want to **make a decision based on the structure of complex data and possibly destructure it at the same time**. This approach can help you adopt a more declarative coding style, which is especially beneficial if you’re following the functional programming paradigm.

In contrast, if you’re making a decision **based on complex business rules** that require a lot of computation, especially if the conditions are non-exclusive or incremental, then you may be better off choosing a different language construct. There are some well-established and usually more appropriate idioms in Python for such scenarios, like a chain of if...elif... statements.

## Key Topics

**Soft Keywords** in Python 3.10 and later, my understanding: it is only for backward compatibility

**match statement** - subject

**case clauses** - structural pattern