from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from wapp.lib.models.session_stock_association import SessionStock
from wapp.lib.portfolio import get_portfolio
from wapp.lib.models import db
from .ticker.blueprint import blueprint as ticker_blueprint

blueprint = Blueprint('portfolio', __name__)
blueprint.register_blueprint(ticker_blueprint, url_prefix='/<ticker>')


@blueprint.get('/')
@jwt_required()
def portfolio():
    user_id = get_jwt_identity()
    portfolio = get_portfolio(user_id)
    return jsonify(portfolio), 200

@blueprint.post('/')
@jwt_required()
def update_portfolio():
    user_id = get_jwt_identity()
    ticker = request.json.get('ticker')
    
    if not ticker:
        return jsonify({"error": "Missing ticker"}), 400
    
    if SessionStock.query.filter_by(session_id=user_id, ticker=ticker).first():
        return jsonify({"error": "Ticker already exists"}), 400
    
    session_stock = SessionStock(
        session_id=user_id,
        ticker=ticker,
        quantity=1,
    )
    
    db.session.add(session_stock)
    db.session.commit()
    
    return {"message": "OK"}, 200
