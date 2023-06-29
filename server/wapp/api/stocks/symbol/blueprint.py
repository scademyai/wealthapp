from flask import Blueprint, jsonify, request, current_app
from wapp.lib.stocks import get_stock, get_stocks

blueprint = Blueprint('symbol', __name__)

@blueprint.route('/<symbol>', methods=['GET'])
def get_stock_route(symbol):
    
    if res := validate_symbol(symbol):
        return res

    # Return error if stock_data is None
    stock_data = get_stock(symbol)
    if stock_data is None:
        return jsonify({"error": "NOK"}), 400

    current_app.logger.info(f"Stock symbol: {symbol}")
    return jsonify(stock_data), 200

def validate_symbol(symbol):
    # Validate stock symbol
    if not isinstance(symbol, str) or not symbol.isalnum() or not len(symbol) <= 5:
        current_app.logger.error("Invalid stock symbol.")
        return jsonify({"error": "NOK"}), 400