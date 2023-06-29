
from unittest.mock import MagicMock, patch
from wapp.api.stocks.blueprint import Stock
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

        AssertThat(r.json).IsEqualTo([STOCKS[0]])
        
    def test_no_json_request(self):
        response = self.client.post('/stocks/')
        AssertThat(response.status_code).IsEqualTo(400)
        AssertThat(response.get_json()).IsEqualTo({"error": "NOK"})

    def test_no_symbols_key(self):
        response = self.client.post('/stocks/', json={})
        AssertThat(response.status_code).IsEqualTo(400)
        AssertThat(response.get_json()).IsEqualTo({"error": "NOK"})

    def test_symbols_not_list(self):
        response = self.client.post('/stocks/', json={"symbols": "ABCD"})
        AssertThat(response.status_code).IsEqualTo(400)
        AssertThat(response.get_json()).IsEqualTo({"error": "NOK"})

    def test_invalid_stock_symbol(self):
        response = self.client.post('/stocks/', json={"symbols": ["ABCD1"]})
        AssertThat(response.status_code).IsEqualTo(400)
        AssertThat(response.get_json()).IsEqualTo({"error": "NOK"})

    @patch('wapp.api.stocks.blueprint.get_stocks')
    def test_valid_request(self, mock_get_stocks):
        mock_get_stocks.return_value = {"ABCD": {"price": 100, "volume": 5000}}
        response = self.client.post('/stocks/', json={"symbols": ["ABCD"]})
        AssertThat(response.status_code).IsEqualTo(200)
        AssertThat(response.get_json()).IsEqualTo({"ABCD": {"price": 100, "volume": 5000}})

    @patch('wapp.api.stocks.blueprint.get_stocks')
    def test_get_stocks_returns_none(self, mock_get_stocks):
        mock_get_stocks.return_value = None
        response = self.client.post('/stocks/', json={"symbols": ["ABCD"]})
        AssertThat(response.status_code).IsEqualTo(400)
        AssertThat(response.get_json()).IsEqualTo({"error": "NOK"})
