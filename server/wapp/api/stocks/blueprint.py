from flask import Blueprint, jsonify, request, current_app
from wapp.lib.stocks import get_stock, get_stocks
from .symbol.blueprint import blueprint as symbol_blueprint

blueprint = Blueprint('stocks', __name__)
blueprint.register_blueprint(symbol_blueprint, url_prefix='/')

class Stock:
    @blueprint.route('/', methods=['GET'])
    def get_stocks_route():
        
         # Get "symbols" from query parameters
        symbols_str = request.args.get("symbols")
        
        # Check if "symbols" query parameter exists
        if symbols_str is None:
            current_app.logger.error("Invalid request format.")
            return jsonify({"error": "NOK"}), 400

        # Split symbols string into a list
        symbols = symbols_str.split(',')

        # Validate stock symbols
        for symbol in symbols:
            if not isinstance(symbol, str) or not symbol.isalnum() or not len(symbol) <= 5:
                current_app.logger.error("Invalid stock symbol.")
                return jsonify({"error": "NOK"}), 400

        # return error if stock_data contains None elements
        stock_data = list(filter(lambda x: x is not None , get_stocks(symbols)))

        current_app.logger.info(f"Stock symbols: {symbols}")
        return jsonify(stock_data), 200
