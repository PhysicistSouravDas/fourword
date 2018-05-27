from flask import Blueprint
from flask import render_template

user = Blueprint('user',__name__)

@user.route('/<userid>', methods=['GET'])
def homepage(userid):
    return "<h2>This is Word Submission page for {}</h2>".format(userid)