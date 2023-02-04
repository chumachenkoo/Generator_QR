from app import db
from models.user import User


def get_user_by_mail(email):
    data = db.session.query(User).filter_by(email=email).all()
    return data


def get_user_by_id(user_id):
    data = db.session.query(User).filter_by(id=user_id).all()
    return data