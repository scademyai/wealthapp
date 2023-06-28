
from unittest.mock import MagicMock, patch
from wapp.api.stocks.blueprint import stock
from wapp.lib.stocks import STOCKS
from truth.truth import AssertThat

from tests import AppTestCase, DbMixin, TestClientMixin


class TestStocks(TestClientMixin, DbMixin, AppTestCase):     
    def test_stocks_returns_list(self):
        r = self.client.post("/stocks/", json={ "symbols": [] })

        AssertThat(r.json).IsInstanceOf(list)

    def test_stocks_returns_filtered_stocks(self):
        r = self.client.post("/stocks/", json={ "symbols": ["TSLA", "AAPL"]})

        AssertThat(r.json).IsEqualTo(STOCKS[:2])

    def test_stocks_returns_a_stock_if_symbols_contains_one_item(self):
        r = self.client.post("/stocks/", json={ "symbols": ["TSLA"]})

        AssertThat(r.json).IsEqualTo(STOCKS[0])
        
    @patch('wapp.api.stocks.blueprint.stock.getstocks', MagicMock(return_value=test_stocks_returns_list))
    def test_stocks_calls_get_stock(self):
        r = self.client.post("/stocks/", json={ "symbols": ["TSLA", "AAPL"]})
        stock.getstocks()
        stock.getstocks.assert_called_once_with()
        
