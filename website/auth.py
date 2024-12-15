from flask import Blueprint, render_template, redirect, url_for
from flask import request, flash
from flask_login import login_user, logout_user, current_user, login_required
from .model import User,Product
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['POST','GET'])
def login():

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        # Check login information
        if user:
            if check_password_hash(user.password,password):
                login_user(user,remember=True)
                # print('login', current_user.id)
                flash(message='Login successfully!',category='success')
                return redirect(url_for('views.home'))
            
            else:
                flash(message='Wrong password!',category='error')
        else:
            flash(message='User doesnt exist!',category='error')

    return render_template('login.html',user=current_user)

@auth.route('/signup',methods=['POST','GET'])
def signup():

    if request.method=='POST':

        email = request.form.get('email')
        name = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        role = request.form.get('role')

        # check signup information
        if password1 == password2:
            
            flash(message='Sign up Successfully!', category='success')

            new_user = User(email=email, name=name, password=generate_password_hash(password1, method='scrypt'),role=role)

            db.session.add(new_user)
            db.session.commit()

            login_user(new_user,remember=True)
            return redirect(url_for('views.home'))

            # return {'name':new_user.name}
        
        else:
            flash(message='Fail to sign up!', category='error')
    
    return render_template('signup.html',user=current_user)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('views.home'))