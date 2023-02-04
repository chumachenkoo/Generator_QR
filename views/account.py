from flask import session, render_template, redirect, url_for
from account.authentication import get_user_by_id
from generator.decode import decode


def user_account():
    if 'id' in session:
        user_id = session.get('id')
        user_data = get_user_by_id(user_id)
        qr = decode(user_data)
        return render_template('account.html', user=user_data, qr_codes=qr)

    return redirect(url_for('get_login'))