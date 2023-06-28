from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def import_models():
    from . import sessions # noqa
    from . import session_stock_association # noqa
def init_db(app):
    
    import_models()
    
    db.init_app(app)
