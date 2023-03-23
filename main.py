import os
import re
from flask import Flask,render_template,redirect,request
from flask.helpers import get_load_dotenv, total_seconds
from model1 import db,Feedback

app = Flask(__name__,template_folder='templates')
app.secret_key = 'super secret key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/aboutus')
def about():
    return render_template('aboutus.html')

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        location=request.form['dropdown']
        ordertype=request.form['papa']
        improvement1=request.form.getlist('improve')
        improvement= ''  
        for i in improvement1:
            improvement = improvement + i + ','
        
        message=request.form['message']
        
        
        feedback = Feedback(name=name,email=email,location=location,improvement=improvement,ordertype=ordertype,message=message)

        db.session.add(feedback)
        db.session.commit()
        return render_template('/')
    else:
        return render_template('feedback.html')


if __name__ == '__main__':
    app.run(debug = True)