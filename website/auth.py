from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>logout<p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 8:
                flash('Passwords must be at least 8 characters long.', category='error')
        else:
            new_user = User(email=email, username=username, password= generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.commit()
            login_user(new_user, remember=True)
            flash('Account Successfully Created!', category='success' )
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")