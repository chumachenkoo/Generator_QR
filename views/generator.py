from flask import session, request, redirect, url_for, render_template
from app import db
from generator.generator import generate


def qr_generator():
    if 'id' in session:
        if request.method == 'POST':
            data = request.form['qr_code']
            user = session.get('id')
            qr = generate(data, user)

            db.session.add(qr)
            db.session.commit()

            return redirect(url_for('user_account'))
        else:
            return render_template('generator.html')
    return redirect(url_for('get_login'))