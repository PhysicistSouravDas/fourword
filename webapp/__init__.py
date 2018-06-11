from flask import Flask, render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from webapp.views.home import home
import pymysql

class Server(object):

    def __init__(self,name=__name__):
        self.app = Flask(name)
        pymysql.install_as_MySQLdb()
        self.db = SQLAlchemy()

    def init_server(self):
        
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/dadwalakshay'
        #self.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://dadwalakshay:itsaweakpassword@dadwalakshay.mysql.pythonanywhere-services.com/dadwalakshay$tundil'
        self.db.init_app(self.app)
        self.blueprints(self.app)
        self.otherroutes(self.app)
        return self.app

    def blueprints(self,app):
        app.register_blueprint(home,url_prefix='/v0.01')

    def otherroutes(self,app):

        @app.errorhandler(404)
        def not_found(errors):
            return render_template('not_found.html'),404

        @app.errorhandler(500)
        def server_error(errors):
            return render_template('error.html'),500

        @app.route('/')
        def entry():
            return redirect(url_for('home.homepage'))