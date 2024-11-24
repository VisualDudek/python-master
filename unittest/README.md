# unittest

## FAQ
- how to test that given string was printed out on stdout? -> mock stdout (004)
- if I patch builtins.input how to test not one but several side_effect?
- how to test builtins.exit, how to test that exit was called? (002)
- what is the diff between `side_effect` and `return_value`?


## Takeaway
- you can use `patch` with `assert` for quick and simple patch, without `unittest.TestCase` (003)
- you can check which args mock object was called using `Mock.call_args.args` (003)
- you can set verbosity `unittest.main(verbosity=2)` (004)
- use help string, visible at verbosity 2 (004)