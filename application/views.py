from flask import Flask, render_template, abort, session, flash, redirect, request
from main import app

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')
