"""
init file for jenweb
"""

import os

from flask import Flask

def create_app(test_config=None):
    # create and config application
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATEBASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )
    if test_config is None:
        # load instance_config if not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load config from test when passed
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # hello world page
    @app.route('/hello')
    def hello():
        return("Oh, Hello.. World")

    return(app)
