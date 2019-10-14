from main import app
import forms
from flask import render_template, abort, session, flash, redirect, request, jsonify
from flask_jwt import JWT, jwt_required, current_identity
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import user

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            return abort(400)
        elif user.is_authenticate(username, password):
            session['username'] = username
            session['logged_in'] = True
            #session['auth_token'] = "someTokenThatWillBeAddedLater"
            return redirect("/files")
        else:
            flask.flash("login fail")
            return redirect("/")

    elif request.method == 'GET':
        logout()
        form = forms.LoginForum()
        return render_template('login.html', form=form)
    else:
        return abort(400)
    return redirect("/login")

@app.route("/files")
def files():
    if not user_logged_in():
        return redirect('/')
    if request.method == 'GET':
        dir = ['filename','filename2']
        return render_template('tables.html', files=dir)
    else:
        return redirect('/')


@app.route('/logout')
@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect("/")


@app.errorhandler(404)
def page_not_found(e):
    # set 404 status explicitly
    return render_template('404.html'), 404

def user_logged_in():
    return 'username' in session
