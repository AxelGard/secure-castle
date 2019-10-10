from main import app
import forms
from flask import render_template, abort, session, flash, redirect, request
from flask_jwt import JWT, jwt_required, current_identity
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import user

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            return abort(400)
        if user.is_authenticate(username, password):
            user.authenticate(username, password)
            flash('You were successfully logged in')
            access_token = create_access_token(identity=username)
            return redirect("/files"), jsonify(access_token=access_token), 200
        else:
            flash('Login failed')
            return redirect("/")

    elif request.method == 'GET':
        logout()
        form = forms.LoginForum()
        return render_template('login.html', form=form)
    else:
        return abort(400)

@app.route("/files")
@jwt_required
def files():
    return "files"


@app.route('/logout')
@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect("/")


@app.route('/error/<error_code>/<error_msg>')
@app.route('/error/<error_code>/<error_msg>/')
def show_error(error_code, error_msg):
    if 'username' in session:
        return "<h1>Error" + error_code + "</h1>" + error_msg
