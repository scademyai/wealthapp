
from unittest.mock import MagicMock, patch
from wapp.api.stocks.blueprint import Stock
from wapp.lib.stocks import STOCKS
from truth.truth import AssertThat

from tests import AppTestCase, DbMixin, TestClientMixin


class TestStocks(TestClientMixin, DbMixin, AppTestCase):     
    def setUp(self):
        super().setUp()

        self.mock_data = [
            {
                "ticker": "TSLA",
                "price": "270.00",
            },
            {
                "ticker": "AAPL",
                "price": "200.00",
            }
        ]

    def test_stocks_returns_list(self):
        r = self.client.get("/stocks/?symbols=aapl,tsla")

        AssertThat(r.json).IsInstanceOf(list)

    @patch("wapp.api.stocks.blueprint.get_stocks")
    def test_stocks_returns_filtered_stocks(self, mock_get_stocks):
        mock_get_stocks.return_value = self.mock_data
        r = self.client.get("/stocks/?symbols=tsla,aapl")

        AssertThat(r.json).IsEqualTo(self.mock_data)

    @patch("wapp.api.stocks.blueprint.get_stocks")
    def test_stocks_returns_a_stock_if_symbols_contains_one_item(self, mock_get_stocks):
        mock_get_stocks.return_value = [self.mock_data[0]]
        r = self.client.get("/stocks/?symbols=tsla")

        AssertThat(r.json).IsEqualTo([self.mock_data[0]])
        
    def test_no_symbols_param(self):
        response = self.client.get('/stocks/')
        AssertThat(response.status_code).IsEqualTo(400)      
        AssertThat(response.get_json()).IsEqualTo({"error": "NOK"})

    def test_symbols_empty_list_item(self):
        response = self.client.get('/stocks/?symbols=tsla,')
        AssertThat(response.status_code).IsEqualTo(400)
        AssertThat(response.get_json()).IsEqualTo({"error": "NOK"})

    def test_invalid_stock_symbol(self):
        response = self.client.get('/stocks/?symbols=abcd11')
        AssertThat(response.status_code).IsEqualTo(400)
        AssertThat(response.get_json()).IsEqualTo({"error": "NOK"})

    @patch('wapp.api.stocks.blueprint.get_stocks')
    def test_get_stocks_returns_empty_list(self, mock_get_stocks):
        mock_get_stocks.return_value = []
        response = self.client.get('/stocks/?symbols=abcd')
        AssertThat(response.status_code).IsEqualTo(200)
        AssertThat(response.get_json()).IsEqualTo([])
   
