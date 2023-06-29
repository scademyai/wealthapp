
from unittest.mock import MagicMock, patch
from truth.truth import AssertThat

from tests import AppTestCase, DbMixin, TestClientMixin


class TestFactoryHttp(TestClientMixin, DbMixin, AppTestCase):
    def test_root_returns_404(self):
        r = self.client.get("/")

        AssertThat(r.status_code).IsEqualTo(404)

    @patch("wapp.factory.create_session", MagicMock())
    def test_login_returns_jwt(self):
        r = self.client.get("/login")

        AssertThat(r.status_code).IsEqualTo(200)
        AssertThat(r.json).ContainsKey("access_token")

    @patch("wapp.api.stocks.blueprint.get_stocks", )
    def test_stocks_returns_stocks(self, stocks_mock):
        stocks_mock.return_value=[{"ticker": "TSLA"}]

        r = self.client.get("/stocks/?symbols=TSLA")
        
        AssertThat(r.status_code).IsEqualTo(200)
        AssertThat(r.json).ContainsExactly({"ticker": "TSLA"})
        AssertThat(stocks_mock.call_args[0][0]).ContainsExactly("TSLA")
