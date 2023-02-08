from flask import request, redirect, session, url_for, render_template
from account.authentication import get_user_by_mail


def post_login():
    if request.method == 'POST':
        user_email = request.form['email']
        user_password = request.form['password']

        user = get_user_by_mail(user_email)

        if len(user) != 0 and user_password == user[0].password:
            session['id'] = user[0].id
            return redirect(url_for('user_account'))

        return redirect(url_for('get_login'))


def get_login():
    if 'id' in session:
        return redirect(url_for('user_account'))
    else:
        return render_template('login.html')


def logout():
    session.clear()
    return redirect(url_for("get_login"))