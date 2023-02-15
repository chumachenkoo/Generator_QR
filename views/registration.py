from flask import session, redirect, url_for, render_template, flash
from models.user import User
from app import db
from forms.registration import RegistrationForm
from sqlalchemy.exc import IntegrityError


def get_registration():
    if 'id' in session:
        return redirect(url_for('user_account'))

    form = RegistrationForm()
    return render_template('registration.html', form=form)


def post_registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            user = User(username=form.username.data,
                        email=form.email.data,
                        password=form.password.data)
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash('User has already been registered!')
        else:
            flash('You have successfully registered!')
            return redirect(url_for('get_login'))
    flash('Use valid data!')
    return redirect(url_for('get_registration'))

