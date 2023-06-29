from flask import Blueprint, jsonify, request, current_app
from wapp.lib.stocks import get_stocks

blueprint = Blueprint('stocks', __name__)

class Stock:
    @blueprint.route('/', methods=['POST'])
    def get_stocks_route():
        # Check if request has a JSON content type
        if not request.is_json:
            current_app.logger.error("Invalid request format.")
            return jsonify({"error": "NOK"}), 400

        # Check if "symbols" key exists in the request body
        symbols = request.json.get("symbols")
        if symbols is None:
            current_app.logger.error("Invalid request format.")
            return jsonify({"error": "NOK"}), 400

        # Check if "symbols" value is a list
        if not isinstance(symbols, list):
            current_app.logger.error("Invalid request format.")
            return jsonify({"error": "NOK"}), 400

        # Validate stock symbols
        for symbol in symbols:
            if not isinstance(symbol, str) or not symbol.isalnum() or not len(symbol) <= 5:
                current_app.logger.error("Invalid stock symbol.")
                return jsonify({"error": "NOK"}), 400

        # return error if stock_data contains None elements
        stock_data = list(filter(lambda x: x is not None , get_stocks(symbols)))

        current_app.logger.info(f"Stock symbols: {symbols}")
        return jsonify(stock_data), 200
