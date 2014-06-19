from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from app import db
from app.users.forms import RegisterForm, LoginForm
from app.users.models import User
from app.users.decorators import requires_login, logout_user

mod = Blueprint('users', __name__, url_prefix='/users')

@mod.route('/me/')
@requires_login
def home():
  #return render_template("users/profile.html", user=g.user)
  return redirect('/')

@mod.before_request
def before_request():
  """
  pull user's profile from the database before every request are treated
  """
  g.user = None
  if 'user_id' in session:
    #g.user = User.query.get(session['user_id'])
    print "session user_id: %s" % (session['user_id'])

@mod.route('/login/', methods=['GET', 'POST'])
def login():
  """
  Login form
  """
  form = LoginForm(request.form)
  # make sure data are valid, but doesn't validate password is right
  if form.validate_on_submit():
    #user = User.query.filter_by(email=form.email.data).first()
    try:
      user = User.objects.get(email=form.email.data)    
      # we use werzeug to validate user's password
      if check_password_hash(user.password, form.password.data): #optional: bool(user)
        # the session can't be modified as it's signed, 
        # it's a safe place to store the user id
        session['user_id'] = str(user.id)
        #flash('Success! Welcome %s!' % user.name)
        return redirect(url_for('home'))
    except:
      flash('Wrong email or password', 'error-message')
  return render_template("users/login.html", form=form)

@mod.route('/logout/')
def logout():
  """
  Remove user from session.
  """
  logout_user()
  return redirect('/')

@mod.route('/register/', methods=['GET', 'POST'])
def register():
  """
  Registration Form
  """
  form = RegisterForm(request.form)
  if form.validate_on_submit():
    # create an user instance not yet stored in the database
    user = User(username=form.name.data, email=form.email.data, \
      password=generate_password_hash(form.password.data))
    # Insert the record in our database and commit it
    user.save()
    #db.session.add(user)
    #db.session.commit()

    # Log the user in, as he now has an id
    session['user_id'] = str(user.id)
    print "session user_id: %s" % (str(user.id))
    # flash will display a message to the user
    #flash('Thanks for registering')
    # redirect user to the 'home' method of the user module.
    return redirect(url_for('users.home'))
  return render_template("users/register.html", form=form)
