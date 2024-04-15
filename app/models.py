from app import db

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    submission_date = db.Column(db.DateTime, nullable=False)
    event_date = db.Column(db.DateTime, nullable=False)
    requester_name = db.Column(db.String(100), nullable=False)
    organization = db.Column(db.String(100), nullable=False)
    room_preference = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='Pending')
