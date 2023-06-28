from wapp.lib.models import db
from wapp.lib.models.sessions import Session


def create_session(session_id):
    session = Session(id=session_id)
    db.session.add(session)
    db.session.commit()
