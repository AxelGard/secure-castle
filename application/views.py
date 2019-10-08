from main import app
import forms
from flask import render_template, abort, session, flash, redirect, request

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
@app.route('/login/', methods=['GET', 'POST'])
def login():
    logout()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            return abort(400)
        
    elif request.method == 'GET':
        form = forms.LoginForum()
        return render_template('login.html', form=form)
    else:
        return abort(400)


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
