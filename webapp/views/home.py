from flask import Blueprint
from flask import render_template, request,redirect,url_for

home = Blueprint('home',__name__,template_folder='../templates')

@home.route('/', methods=['GET'])
def homepage():
	from webapp.logic.brain import Brain
	words = Brain().extract_words()
	Brain().word_cloud(words)
	return render_template('home.html',clouddata = words)

@home.route('/wow', methods=['GET'])
def wot():
    return render_template('userform.html')

@home.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@home.route('/usereq', methods=['POST'])
def usereq():
	from webapp.logic.brain import Brain #i was getting error in this line as it was trying to import Server class before its initialization
	w1 = request.form['usereq1']
	w2 = request.form['usereq2']
	w3 = request.form['usereq3']
	w4 = request.form['usereq4']
	uip = request.environ['REMOTE_ADDR']
	Brain().store_words(w1,w2,w3,w4,uip)
	return redirect(url_for('home.feedback'))

@home.route('/feedback',methods=['GET'])
def feedback():
	return render_template('feedback.html')

@home.route('/userfeed',methods=['POST'])
def userfeed():
	from webapp.logic.brain import Brain
	feed = request.form['userfeed']
	uip = request.environ['REMOTE_ADDR']
	Brain().store_feed(feed,uip)
	return redirect(url_for('home.homepage'))

	