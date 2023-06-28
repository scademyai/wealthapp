from sqlalchemy.dialects.postgresql import UUID

from . import db

class SessionStock(db.Model):
    __tablename__ = "session_stock"
    __table_args__ = (
        db.UniqueConstraint("session_id", "ticker", name="unique_config"),
    )


    session_id = db.Column(UUID(as_uuid=True), db.ForeignKey("sessions.id"), primary_key=True)
    ticker = db.Column(db.String(5), primary_key=True)

    session = db.relationship("Session", backref="session_stocks")
    
    quantity = db.Column(db.Integer, nullable=False)
    
    
    def __repr__(self):
        return "<SessionStock(session_id={session_id}, ticker={ticker})>".format(
            session_id=self.session_id,
            ticker=self.ticker,
        )
