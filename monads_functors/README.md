# Monads and Functors

**Functor** Imagine you have a box(`Functor`) containing a value. You can paint the value using `map` function, but the box reamains the same.
**Endofunctor**
**Monad** A monad is like a box where, during operation, you can return a new box or decide to return nothing, depending on the operation.
- have unit type operation
- "Maybe", "List", "Either", "Writer", "State", "IO", "Reader" 
- there is (1)Left and (2)Right identity and (3)Associativity


**Railroad-oriented** programming 

**Pattern matching** as core of Railroad-oriented logic

## Takeaway

- `f(g(h(x)))` represent function compostion (001)
- sequance of functions vs. composition, first one is more readable (001) 
- functor return functor with value wraped into func. (001)
- Unlike functors, monad bind method do not by-self return monad, we expect that bind function will return monad (002)
- you can use lambda in `.bind` method to ensure that return is type `Monad` (002)
- you can translate python exeption error handling into monadic error handling model (004)
- very clean and readable business logic of Railroad and Pattern matching (004)
