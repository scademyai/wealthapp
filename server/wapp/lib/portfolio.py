from wapp.lib.stocks import get_stock
from wapp.lib.models.session_stock_association import SessionStock


def get_portfolio(user_id):
    session_stocks_list = []
    for session_stock in  SessionStock.query.filter_by(session_id=user_id).all():
        session_stocks_list.append({
            "ticker": session_stock.ticker,
            "quantity": session_stock.quantity,
            "price": get_stock(session_stock.ticker).get("price"),
        })
    return session_stocks_list
