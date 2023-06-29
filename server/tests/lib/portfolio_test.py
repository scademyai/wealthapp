from truth.truth import AssertThat

from tests import AppTestCase, DbMixin
from wapp.lib.models.session_stock_association import SessionStock
from wapp.lib.models.sessions import Session
from wapp.lib.portfolio import get_portfolio
from wapp.lib.models import db

class TestPortfolio(DbMixin, AppTestCase):
    def test_get_portfolio_returns_users_portfolio(self):
        session = Session(id="00000000-0000-0000-0000-000000000000")
        session2 = Session(id="00000000-0000-0000-0000-000000000001")
    
        session_stock = SessionStock(
            session_id=session.id,
            ticker="AAPL",
            quantity=1,
        )
        session_stock2 = SessionStock(
            session_id=session2.id,
            ticker="TSLA",
            quantity=2,
        )
        
        db.session.add(session)
        db.session.add(session2)
        db.session.add(session_stock)
        db.session.add(session_stock2)
        db.session.commit()
        
        portfolio = get_portfolio(session.id)
        
        AssertThat(portfolio[0].get("ticker")).IsEqualTo("AAPL")
        AssertThat(portfolio[0].get("quantity")).IsEqualTo(1)

