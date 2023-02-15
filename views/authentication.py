from flask import redirect, session, url_for, render_template, flash
from account.authentication import get_user_by_mail
from forms.authentication import LoginForm


def post_login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = get_user_by_mail(email)
        if user and password == user[0].password:
            session['id'] = user[0].id
            return redirect(url_for('user_account'))

    flash('Use valid data')
    return redirect(url_for('get_login'))


def get_login():
    if 'id' in session:
        return redirect(url_for('user_account'))
    else:
        form = LoginForm()
        return render_template('login.html', form=form)


def logout():
    session.clear()
    return redirect(url_for("get_login"))

