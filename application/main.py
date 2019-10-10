# flask
from flask import Flask, escape, request
from flask_cachebuster import CacheBuster

#JWT
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import user

#logging
import os
import logging
import logging.handlers

def create_server():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    file_handler = logging.handlers.RotatingFileHandler('errorlog.txt')
    app.logger.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)
    return app

app = create_server()
from views import *

def cache_buster():
    """ css cache buster """
    config = { 'extensions':['.js', '.css'], 'hash_size': 5 }
    cache_buster = CacheBuster(config=config)
    cache_buster.init_app(app)


# run server
if __name__ == "__main__":
    print(" * starting --> secure-castle")
    cache_buster()
    jwt = JWT(app, user.authenticate, user.identity)
    app.run(debug=app.config['DEBUG'], port=app.config['PORT'])
