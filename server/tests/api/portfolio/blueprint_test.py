
from unittest.mock import MagicMock, patch
import uuid
from wapp.lib.models.session_stock_association import SessionStock
from wapp.api.portfolio.blueprint import portfolio
from truth.truth import AssertThat
from wapp.lib.models import db

from flask_jwt_extended import decode_token

from tests import AppTestCase, TestClientMixin, DbMixin

class TestPortfolio(TestClientMixin, DbMixin, AppTestCase):
    def test_portfolio_returns_list(self):
        r = self.client.get("/login")
        headers = { "Authorization": f"Bearer {r.json['access_token']}" }
        r = self.client.get("/portfolio/", headers=headers)

        AssertThat(r.json).IsInstanceOf(list)
        
    @patch('wapp.api.portfolio.blueprint.get_portfolio')
    def test_portfolio_get_returns_users_portfolio_in_request_body(self, get_portfolio_mock):
        
        get_portfolio_mock.return_value = [
            {
                "id": "00000000-0000-0000-0000-000000000000",
                "ticker": "TEST",
                "quantity": 1
            }
        ]
        
        r = self.client.get("/login")
        headers = { "Authorization": f"Bearer {r.json['access_token']}" }
        r = self.client.get("/portfolio/", headers=headers)
        
        AssertThat(r.json).IsEqualTo([
            {
                "id": "00000000-0000-0000-0000-000000000000",
                "ticker": "TEST",
                "quantity": 1,
            }
        ])

    def test_update_portfolio_add_new_ticker(self):
        r = self.client.get("/login")
        headers = { "Authorization": f"Bearer {r.json['access_token']}" }
        user_id = decode_token(r.json['access_token'])["sub"]
        
        response = self.client.post('/portfolio/', json={"ticker": "AAPL"}, headers=headers)
        
        session_stock = SessionStock.query.filter_by(session_id=user_id, ticker="AAPL").first()
        
        AssertThat(response.status_code).IsEqualTo(200)
        AssertThat(session_stock.quantity).IsEqualTo(1)
        AssertThat(session_stock.ticker).IsEqualTo("AAPL")
