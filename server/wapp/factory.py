from datetime import timedelta, datetime
import json
import os
from uuid import uuid4

from flask import (
    Flask,
    after_this_request,
    jsonify,
    request
)
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
)
from wapp.lib.session import create_session
from wapp.api.stocks.blueprint import blueprint as stocks_blueprint

def __configure_cors(app):
    CORS(app, origins=["http://localhost:4200"])


def __init_db(app):
    app.config.from_file('config.json', load=json.load)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
    app.config["DATABASE_URL"] = os.environ["DATABASE_URL"]

    from wapp.lib.models import init_db

    init_db(app)
    
def __configure_access_token(app):
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1825)

def __register_blueprints(app):
    app.register_blueprint(stocks_blueprint, url_prefix="/stocks")

def create_app():
    app = Flask(__name__, static_folder="./client/dist")
    app.secret_key = "very-secret-key"

    __configure_access_token(app)
    __configure_cors(app)
    __init_db(app)
    JWTManager(app)

    __register_blueprints(app)
    
    @app.route("/login", methods=["GET"])
    def login():
        session_id = uuid4()
        access_token = create_access_token(identity=session_id)
        create_session(session_id)

        @after_this_request
        def set_access_token(response):
            response.headers["Access-Token"] = access_token
            return response

        return jsonify(access_token=access_token)

    return app


if __name__ == "__main__":
    create_app()
