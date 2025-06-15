# Design pattern Strategy

- `01` - first problem is that for both strategies there are hrdcoded parameters, (1) for Average there is hardcoded window size and (2) for MinMax there are hardcoded lvl. of prices
- ^^^ you can solve it by using `**kwargs` but this is not good choice
- you can create union of strategy parameters as dataclass `StrategyParameters` and pass as var to all methods BUT it add coupling between Strategies -> it is not CLEAR which parameter belogs to what strategy. 
- "Parameters per strategy" - just convert implementation of each TradingStrategy into dataclass and add parameters as attributes `02`, TAKEAWAY: combine behavior with data at the source of behavior using dataclass