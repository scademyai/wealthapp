from wapp.lib.models.session_stock_association import SessionStock
from truth.truth import AssertThat
from wapp.lib.models import db

from flask_jwt_extended import decode_token

from tests import AppTestCase, TestClientMixin, DbMixin

class TestPortfolio(TestClientMixin, DbMixin, AppTestCase):
    def test_delete_stock_from_portfolio_non_existent_stock(self):
        r = self.client.get("/login")
        headers = { "Authorization": f"Bearer {r.json['access_token']}" }
        
        response = self.client.delete('/portfolio/NONEX/', headers=headers)
        AssertThat(response.status_code).IsEqualTo(404)
    
    def test_delete_stock_from_portfolio_success(self):
        r = self.client.get("/login")
        headers = { "Authorization": f"Bearer {r.json['access_token']}" }
        user_id = decode_token(r.json['access_token'])["sub"]
        
        test_ticker = SessionStock(session_id=user_id, ticker="AAPL", quantity=1)
        db.session.add(test_ticker)
        db.session.commit()

        response = self.client.delete('/portfolio/AAPL/', headers=headers)
        AssertThat(response.status_code).IsEqualTo(200)

        deleted_stock = SessionStock.query.filter_by(session_id=user_id, ticker="AAPL").first()
        AssertThat(deleted_stock).IsNone()

    def test_update_portfolio_missing_diff(self):
        r = self.client.get("/login")
        headers = { "Authorization": f"Bearer {r.json['access_token']}" }
        
        response = self.client.put('/portfolio/TEST/', json={}, headers=headers)
        AssertThat(response.status_code).IsEqualTo(400)
        AssertThat(response.json).ContainsKey("error")
        AssertThat(response.json["error"]).IsEqualTo("Missing diff")
        
    def test_update_portfolio_increase_quantity(self):
        r = self.client.get("/login")
        headers = { "Authorization": f"Bearer {r.json['access_token']}" }
        user_id = decode_token(r.json['access_token'])["sub"]
        
        test_ticker = SessionStock(session_id=user_id, ticker="AAPL", quantity=1)
        db.session.add(test_ticker)
        db.session.commit()

        response = self.client.put('/portfolio/AAPL/', json={"diff": 1}, headers=headers)
        
        session_stock = SessionStock.query.filter_by(session_id=user_id, ticker="AAPL").first()
        
        AssertThat(response.status_code).IsEqualTo(200)
        AssertThat(session_stock.quantity).IsEqualTo(2)
        AssertThat(session_stock.ticker).IsEqualTo("AAPL")

    def test_update_portfolio_decrease_quantity(self):
        r = self.client.get("/login")
        headers = { "Authorization": f"Bearer {r.json['access_token']}" }
        user_id = decode_token(r.json['access_token'])["sub"]
        
        test_ticker = SessionStock(session_id=user_id, ticker="AAPL", quantity=3)
        db.session.add(test_ticker)
        db.session.commit()

        response = self.client.put('/portfolio/AAPL/', json={"diff": -1}, headers=headers)
        
        session_stock = SessionStock.query.filter_by(session_id=user_id, ticker="AAPL").first()
        
        AssertThat(response.status_code).IsEqualTo(200)
        AssertThat(session_stock.quantity).IsEqualTo(2)
        AssertThat(session_stock.ticker).IsEqualTo("AAPL")
