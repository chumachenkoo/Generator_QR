from app import db


class QRcode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qr_code = db.Column(db.LargeBinary, nullable=True)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))