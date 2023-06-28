from sqlalchemy.dialects.postgresql import UUID

from . import db


class Session(db.Model):
    __tablename__ = "sessions"

    id = db.Column(UUID(as_uuid=True), primary_key=True)

    def __repr__(self):
        return "<Session(id={id})>".format(id=self.id)
