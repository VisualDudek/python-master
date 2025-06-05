from dataclasses import dataclass
import statistics
from typing import Protocol

PRICE_DATA = {
    "BTC/USD": [
        35_842,
        34_069,
        33_871,
        34_209,
        32_917,
        33_917,
        33_370,
        34_445,
        32_901,
        33_013,
    ]
}


class ExchangeConnectionError(Exception):
    """Custom error"""


class Exchange:
    def __init__(self):
        self.connected = False

    def connect(self) -> None:
        print("Connecting to Crypto exchange...")
        self.connect = True

    def check_connection(self) -> None:
        if not self.connected:
            raise ExchangeConnectionError()
        
    def get_market_data(self, symbol: str) -> list[int]:
        self.check_connection()
        return PRICE_DATA[symbol]
    
    def buy(self, symbol: str, amount: int) -> None:
        self.check_connection()
        print(f"Buying amount {amount} in maket {symbol}.")

    def sell(self, symbol: str, amount: int) -> None:
        self.check_connection()
        print(f"Selling amount {amount} in maket {symbol}.")


class TradingStrategy(Protocol):
    def should_buy(self, prices: list[int]) -> bool:
        raise NotImplementedError()

    def should_sell(self, prices: list[int]) -> bool:
        raise NotImplementedError()
    

class AverageTradingStrategy:
    def should_buy(self, prices: list[int]) -> bool:
        list_window = prices[-3:]
        return prices[-1] < statistics.mean(list_window)

    def should_sell(self, prices: list[int]) -> bool:
        list_window = prices[-3:]
        return prices[-1] > statistics.mean(list_window)
    

class MinMaxTradingStrategy:
    def should_buy(self, prices: list[int]) -> bool:
        return prices[-1] < 32_000

    def should_sell(self, prices: list[int]) -> bool:
        return prices[-1] > 33_000


@dataclass
class TradingBot:

    exchange: Exchange
    trading_strategy: TradingStrategy

    def run(self, symbol: str) -> None:
        prices = self.exchange.get_market_data(symbol)
