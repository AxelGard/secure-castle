# flask
from flask import Flask, escape, request
from flask_cachebuster import CacheBuster

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

server = create_server()
import views

def cache_buster():
    """ css cache buster """
    config = { 'extensions':['.js', '.css'], 'hash_size': 5 }
    cache_buster = CacheBuster(config=config)
    cache_buster.init_app(server)


# run server
if __name__ == "__main__":
    print(" * starting --> secure-castle")
    cache_buster()
    server.run(debug=server.config['DEBUG'], port=server.config['PORT'])
