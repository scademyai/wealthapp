import unittest
from truth.truth import AssertThat
from wapp.lib.stocks import get_stocks


class TestStocks(unittest.TestCase):
    def test_get_stocks_returns_single_stock(self):
        stocks = get_stocks(["TSLA"])

        AssertThat(stocks).IsEqualTo([{
            "ticker": "TSLA",
            "price": "270.00",
            "volume": "1000000"
        }])
        
    def test_get_stocks_returns_stocks(self):
        stocks = get_stocks(["TSLA", "AAPL"])

        AssertThat(stocks).IsEqualTo([
            {
                "ticker": "TSLA",
                "price": "270.00",
                "volume": "1000000"
            },
            {
                "ticker": "AAPL",
                "price": "200.00",
                "volume": "2000000"
            }
        ])
