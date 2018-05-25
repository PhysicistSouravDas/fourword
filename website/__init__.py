from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from website.views.user import user
from website.views.admin import admin
from website.views.home import home
import pymysql

class Server(object):

    def __init__(self):
        self.db = SQLAlchemy()

    def init_server(self,name=__name__):
        app = Flask(name)
        pymysql.install_as_MySQLdb()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/dadwalakshay'
        self.db.init_app(app)
        self.blueprints(app)
        return app

    def blueprints(self,app):
        app.register_blueprint(home,url_prefix='/')
        app.register_blueprint(user,url_prefix='/user')
        app.register_blueprint(admin,url_prefix='/admin')