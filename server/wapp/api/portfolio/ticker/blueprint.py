from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from wapp.lib.models.session_stock_association import SessionStock
from wapp.lib.models import db

blueprint = Blueprint('ticker', __name__)

@blueprint.delete('/')
@jwt_required()
def delete_stock_from_portfolio(ticker):
    user_id = get_jwt_identity()

    if session_stock := SessionStock.query.filter_by(session_id=user_id, ticker=ticker).first():
        db.session.delete(session_stock)
        db.session.commit()
    else:
        return jsonify({"error": "Ticker not found"}), 404

    return {"message": "OK"}, 200

@blueprint.put('/')
@jwt_required()
def update_stock_quantity(ticker):
    user_id = get_jwt_identity()
    diff = request.json.get('diff')

    if not diff:
        return jsonify({"error": "Missing diff"}), 400

    if session_stock := SessionStock.query.filter_by(session_id=user_id, ticker=ticker).first():
        session_stock.quantity += diff
    else:
        return jsonify({"error": "Ticker not found"}), 404 

    db.session.add(session_stock)
    db.session.commit()

    return {"message": "OK"}, 200
