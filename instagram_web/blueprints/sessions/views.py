from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.user import User
from werkzeug.security import check_password_hash
from flask_login import login_user, login_required, current_user, logout_user

sessions_blueprint = Blueprint('sessions', __name__, template_folder='templates')

@sessions_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('sessions/new.html')

@sessions_blueprint.route('/', methods=['POST'])
def create():
    # option 2: using flask-login
    username = request.form['username']
    user = User.get_or_none(User.username == username)
    if user:
        password = request.form['password']
        hashed_password = user.password
        result = check_password_hash(hashed_password, password)
        if result:
            remember = True if request.form.get('remember') else False
            login_user(user, remember = remember)
            flash("Welcome back! We've missed you.")
            return redirect(url_for("sessions.index"))
        else:
            flash("Uh oh, your username and/or password do not match. Please try again!", "error")
            return render_template('sessions/new.html')
    else:
        flash("Sorry, we couldn't find an account with that username.", 'error')
        return render_template("sessions/new.html")

    # # option 1: manage sessions manually
    # user = User.get_or_none(User.username == request.form['username'])
    # if user:
    #     password_to_check = request.form['password']
    #     hashed_password = user.password
    #     result = check_password_hash(hashed_password, password_to_check)
    #     if result:
    #         session["user_id"] = user.id
    #         flash("Welcome back!")
    #         return redirect(url_for('sessions.test'))
    #     else:
    #         flash("Uh oh, your username and/or password do not match. Please try again!", "error")
    #         return render_template('sessions/new.html', username=request.form['username'])
    # else:
    #     flash("Sorry, we couldn't find an account with that username.", "error")
    #     return render_template('sessions/new.html')

@sessions_blueprint.route('/landing')
@login_required
def index():
    # option 2: using flask-login
    return render_template('sessions/landing.html', name=current_user.username)

    # # option 1: manage sessions manually
    # if 'user_id' in session:
    #     user = User.get_by_id(user_id)
    #     return render_template('sessions/test.html', user=user)
    # else:
    #     flash("Not logged in", "error")
    #     return render_template('sessions/new.html')

@sessions_blueprint.route('/')
@login_required
def destroy():
    # option 2: using flask-login
    logout_user()
    flash('Logout was successful. See you again soon!')
    return redirect(url_for('sessions.new'))

    # # option 1: manage sessions manually
    # session.pop('user_id', None)
    # return redirect(url_for('sessions.new'))
