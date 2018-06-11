from webapp import Server

db = Server().db

class Userinp(db.Model):

    def __init__(self,w1,w2,w3,w4,uip):
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.w4 = w4
        self.uip = uip

    __tablename__ = 'userinp'
    w1 = db.Column(db.String(10))
    w2 = db.Column(db.String(10))
    w3 = db.Column(db.String(10))
    w4 = db.Column(db.String(10))
    uip = db.Column(db.String(16))
    uno = db.Column(db.Integer,primary_key=True,autoincrement = True)

class Userfeed(db.Model):
    def __init__(self,feed,uip):
        self.feed = feed
        self.uip = uip

    __tablename__='userfeed'
    feed = db.Column(db.String(100))
    uip = db.Column(db.String(16))
    uno = db.Column(db.Integer,primary_key=True,autoincrement = True)