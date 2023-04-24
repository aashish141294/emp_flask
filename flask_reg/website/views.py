from flask import Blueprint, render_template, request, flash,redirect,url_for
from flask_login import login_required, current_user
from . import db
from .models import User

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    all_user = User.query.all()
    if request.method == 'POST':
        all_user = User.query.all()
    return render_template("home.html", user=current_user,all_user=all_user)


@views.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id):  
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('views.home'))


@views.route('/update/<int:id>', methods=['GET','POST'])
def update(id):  
    if request.method == 'POST':
      first_name = request.form['first_name']
      email = request.form['email']  
      password1 = request.form['password1']
      password2 = request.form['password1']
      user = User.query.filter_by(id=id).first()
      user.first_name = first_name
      user.email =email
      user.password = password1
      if password1 != password2:
        flash('Passwords don\'t match.', category='error')
      else:
        db.session.add(user)
        db.session.commit()
        flash('User Updated!', category='success')
        return render_template('update.html',user=user)
    user = User.query.filter_by(id=id).first()
    return render_template('update.html',user = user)
 