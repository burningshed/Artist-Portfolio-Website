"""
docstring
"""
from flask import render_template, Blueprint

pages = Blueprint("pages", __name__, template_folder='templates')
@pages.route('/')
def landing():
    return render_template('landing.html')

@pages.route('/about')
def about():
    return render_template('about.html')
