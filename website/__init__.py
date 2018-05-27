from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from website.views.user import user
from website.views.home import home
import pymysql

class Server(object):

    def __init__(self,name=__name__):
        self.app = Flask(name)
        pymysql.install_as_MySQLdb()
        self.db = SQLAlchemy()

    def init_server(self):
        
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/dadwalakshay'
        self.db.init_app(self.app)
        self.blueprints(self.app)
        self.errors(self.app)
        return self.app

    def blueprints(self,app):
        app.register_blueprint(home,url_prefix='/')
        app.register_blueprint(user,url_prefix='/user')

    def errors(self,app):
        @app.errorhandler(404)
        def not_found(errors):
            return render_template('not_found.html'),404

        @app.errorhandler(500)
        def server_error(errors):
            return render_template('server_error.html'),500

        
