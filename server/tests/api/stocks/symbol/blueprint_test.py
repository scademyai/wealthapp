from unittest.mock import patch
from truth.truth import AssertThat

from tests import AppTestCase, DbMixin, TestClientMixin


class TestSymbol(TestClientMixin, DbMixin, AppTestCase):     
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
    
    @patch('wapp.api.stocks.symbol.blueprint.get_stock')
    def test_get_stock_return_symbol(self, mock_get_stock):
        mock_get_stock.return_value = self.mock_data[0]
        response = self.client.get('/stocks/TSLA')
        AssertThat(response.status_code).IsEqualTo(200)
        AssertThat(response.get_json()).IsEqualTo(self.mock_data[0])

    @patch('wapp.api.stocks.symbol.blueprint.get_stock')
    def test_get_stock_invalid_symbol(self, mock_get_stock):
        mock_get_stock.return_value = None
        response = self.client.get('/stocks/INVALID')
        AssertThat(response.status_code).IsEqualTo(400)
