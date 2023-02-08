from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    qr_codes = db.relationship('QRcode', backref='qrcode', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
