# unittest

## FAQ
- how to test that given traing was printed out on stdout?
- if I patch builtins.input how to test not one but several side_effect?
- how to test builtins.exit, how to test that exit was called? (002)
- what is the diff between `side_effect` and `return_value`?


## Takeaway
- you can use `patch` with `assert` for quick and simple patch, without `unittest.TestCase` (003)