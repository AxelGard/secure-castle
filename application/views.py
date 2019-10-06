from flask import render_template, abort, session, flash, redirect, request


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')
