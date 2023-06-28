from flask import Blueprint, jsonify, request, current_app
from wapp.lib.stocks import get_stocks

blueprint = Blueprint('stocks', __name__)
class stock:
    @blueprint.route('/', methods=['POST'])
    def getstocks():
        current_app.logger.info(request.json)
        # Representing the request body as a dictionary
        # request.json is a dictionary       
        # # s represents the value of the key "symbols" in the request body
        s = request.json["symbols"]


        return jsonify(get_stocks(s))
            
            
