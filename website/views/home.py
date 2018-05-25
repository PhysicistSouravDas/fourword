from flask import Blueprint
from flask import render_template

home = Blueprint('home',__name__,template_folder='../templates')

@home.route('/', methods=['GET'])
def homepage():
    return render_template('homepage.html')