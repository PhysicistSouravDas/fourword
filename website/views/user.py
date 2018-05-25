from flask import Blueprint
from flask import render_template

user = Blueprint('user',__name__)

@user.route('/', methods=['GET'])
def homepage():
    return "<h2>This is Homepage.</h2>"

@user.route('/submit', methods=['POST'])
def register():
    return "<h2>Your Words are saved.</h2>"