from flask import Flask
import flask
from flask_sqlalchemy import SQLAlchemy

#basedir = os.path.abspath(os.path.dirname(file))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Feedback(db.Model):

    __tablename__ = 'feedback'

    id = db.Column(db.Integer,nullable=False,primary_key=True)
    name = db.Column(db.String(180),nullable=True)
    email = db.Column(db.String(320),nullable=False)
    location = db.Column(db.String(20),nullable=False)
    ordertype = db.Column(db.String(20),nullable=False)
    improvement = db.Column(db.String(120),nullable=False)
    message = db.Column(db.Text,nullable=True)

    def __init__(self,name,email,location,improvement,ordertype,message):
        self.name=name
        self.email=email
        self.location=location
        self.ordertype=ordertype
        self.improvement=improvement
        self.message= message


db.create_all()
db.session.commit()