from flask import Blueprint
from flask import render_template

admin = Blueprint('admin',__name__)

@admin.route('/', methods=['GET'])
def homepage():
    return "<h2>This is Homepage for Admin.</h2>"

@admin.route('/generate', methods=['POST'])
def register():
    return "<h2>Your wordcloud is generated.</h2>"