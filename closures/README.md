# Closures


In Python, closures are a programming concept where a nested function remembers the values from its enclosing scope, even if that scope has finished executing.

**Why use closures?**
- To maintain state in a fuction without using global variables or classes.
- To create function factories.
- To implement data hiding an encapsulation.

- **Maintaining State** huge gotcha with using `nonlocal`, The nonlocal declaration is used because count is a variable in the enclosing function’s scope (neither local to counter nor global). This allows the inner function to rebind the count variable from the outer scope​ . If count were a mutable object (like a list or dictionary), you could modify it in place without nonlocal​, but since an integer is immutable, nonlocal is required to increment it.
- Real-world use cases: (1) to throttle function calls, or to accumulate values.
- Alternatives can be : global variables, classes.

- **Creating Function Factories** Closures are also useful for creating function factories – higher-order functions that generate customized functions on the fly. The outer function acts as a factory that sets up some configuration or parameter, and the inner function (the closure) uses that configuration when it’s called. This allows you to create multiple specialized functions without repeating code. Each generated function retains the environment in which it was created.
- Real-world example: generating specialized logging or formatting functions: you could write a factory that takes a format string or prefix and returns a logging function that prepends that format to all messages. In general, closures make it easy to package up configuration with behavior, producing concise and customized function objects on demand.

- **Encapsulation and Data Hiding With Closures** troche już naciągane 