from app import db

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, nullable=False)
    description = db.Column(db.String(120), index=True, nullable=False)
    assigned_to = db.Column(db.String(64), index=True, nullable=True)
    status = db.Column(db.Boolean, default=False)