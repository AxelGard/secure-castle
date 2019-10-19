from main import app
import forms
from flask import render_template, abort, session, flash, redirect, request, jsonify, send_file
from flask_jwt import JWT, jwt_required, current_identity
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from werkzeug import secure_filename
import os
import user, file_handler

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
        dir = file_handler.files_in_dir("files/")
        return render_template('tables.html', files=dir)
    else:
        return redirect('/')

@app.route("/newfile", methods=['GET', 'POST'])
def new_file():
    if not user_logged_in():
        return redirect('/')
    elif request.method == 'GET':
        form = forms.File()
        return render_template('upload.html', form=form)
    elif request.method == 'POST':
        path = "files/"
        f = request.files['file']
        path += secure_filename(f.filename)
        f.save(path)
        file_obj = file_handler.File(secure_filename(f.filename), path, "AesCrypt")
        key = str(request.form['key'])
        file_obj.encrypte(key)
        return redirect("/files")
    else:
        return redirect('/')


@app.route("/files/<filename>/download", methods=['GET', 'POST'])
def download_file(filename):
    if not user_logged_in():
        return redirect('/')
    elif request.method == 'GET':
        form = forms.File()
        return render_template('download.html', filename=filename, form=form)

    elif request.method == 'POST':
        # get file
        path = "files/" + filename
        file_obj = file_handler.File(filename, path, "AesCrypt")
        # decrypt
        key = str(request.form['key'])
        file_obj.decrypte(key)

        new_file_name = str(file_obj.name).replace('.aes', '')
        new_file_path = 'files/temp/'
        # if was successful in decrypting file
        if new_file_name in file_handler.files_in_dir(new_file_path):
            new_file_path += new_file_name
            file_obj.remove()
            new_file_obj = file_handler.File(new_file, new_file_path, None)

            return send_file(new_file_obj.path, as_attachment=True), new_file_obj.remove()

        else:
            return redirect("/files/" + filename + "/download")

    else:
        return redirect('/')


@app.route("/files/<filename>/delete", methods=['GET', 'POST'])
def delete_file(filename):
    if not user_logged_in():
        return redirect('/')
    elif request.method == 'GET':
        return render_template('delete.html', filename=filename)

    elif request.method == 'POST':
        path = "files/" + str(filename)
        file_obj = file_handler.File(filename, path, "AesCrypt")
        file_obj.remove()
        return redirect("/files")

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
