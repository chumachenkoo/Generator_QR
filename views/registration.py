from flask import session, redirect, url_for, render_template, request, flash
from models.user import User
from app import db
from account.authentication import get_user_by_mail


def get_registration():
    if 'id' in session:
        return redirect(url_for('user_account'))

    return render_template('registration.html')


def post_registration():
    if request.method == "POST":
        user = User(username=request.form.get('username'),
                    email=request.form.get('email'),
                    password=request.form.get('password'))

        if get_user_by_mail(user.email):
            flash('User has been already registered!')
            return render_template('registration.html')

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('user_account'))