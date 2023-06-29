import unittest
from unittest import mock
from truth.truth import AssertThat
from wapp.lib.stocks import get_stocks, get_stock


class TestStocks(unittest.TestCase):
    @mock.patch('requests.get')
    def test_get_stocks_returns_single_stock(self, mock_get):
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "chart": {
                "result": [
                    {"meta": {"regularMarketPrice": 100.00}}
                ]
            }
        }

        mock_get.return_value = mock_response

        stocks = get_stocks(["TSLA"])

        AssertThat(stocks).IsEqualTo([{
            "ticker": "TSLA",
            "price": 100.00,
        }])
        
    @mock.patch('requests.get')
    def test_get_stocks_returns_stocks(self, mock_get):
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "chart": {
                "result": [
                    {"meta": {"regularMarketPrice": 100.00}}
                ]
            }
        }

        mock_get.side_effect = [mock_response, mock_response]
        stocks = get_stocks(["TSLA", "AAPL"])

        AssertThat(stocks).IsEqualTo([
            {
                "ticker": "TSLA",
                "price": 100.00,
            },
            {
                "ticker": "AAPL",
                "price": 100.00,
            }
        ])

    @mock.patch('requests.get')
    def test_get_stock_valid_ticker(self, mock_get):
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "chart": {
                "result": [
                    {"meta": {"regularMarketPrice": 100.00}}
                ]
            }
        }

        mock_get.return_value = mock_response

        ticker = "AAPL"
        result = get_stock(ticker)
        AssertThat(result).ContainsKey("ticker")
        AssertThat(result).ContainsKey("price")
        AssertThat(result["ticker"]).IsInstanceOf(str)
        AssertThat(result["price"]).IsInstanceOf(float)

    def test_get_stock_invalid_ticker(self):
        ticker = "INVALID"
        result = get_stock(ticker)
        AssertThat(result).IsEqualTo(None)

    def test_get_stock_empty_ticker(self):
        ticker = ""
        result = get_stock(ticker)
        AssertThat(result).IsEqualTo(None)

    def test_get_stock_non_string_ticker(self):
        ticker = 123
        result = get_stock(ticker)
        AssertThat(result).IsEqualTo(None)
