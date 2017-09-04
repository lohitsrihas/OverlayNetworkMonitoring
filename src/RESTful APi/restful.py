from flask import Flask, jsonify, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, flash
from flask_wtf import Form
from flask_login import LoginManager
from flask_login import login_user , logout_user , current_user , login_required
from sqlalchemy.engine import Engine

import datetime

import os

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = os.urandom(24)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:akhi@localhost/test'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column('id',db.Integer , primary_key=True)
    name = db.Column('name', db.String(20), unique=True , index=True)
    username = db.Column('username', db.String(20), unique=True , index=True)
    password = db.Column('password' , db.String(10))
    email = db.Column('email',db.String(50),unique=True , index=True)
 
    def __init__(self ,name , username ,password , email):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
 
    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return True
 
    def get_id(self):
        return unicode(self.id)
 
    def __repr__(self):
        return '<User %r>' % (self.username)
        
    def reload_user(self, callback):
        self.username_callback = callback
        self.password_callback = callback
        return callback

@login_manager.user_loader
def load_user(id):
 return User.query.get(int(id))

@app.route('/', methods=['GET'])

def home():

        return render_template("welcome.html")

@app.route('/register' , methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('signup.html')
    user = User(request.form['name'] , request.form['username'] , request.form['password'],request.form['email'])
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('login'))

@app.route('/account', methods=['GET','post'])        
@login_required
def account():
    if request.method == 'POST':
        user=User.query.filter_by(username=request.form['username'],password=request.form['password']).first()
        user.username = request.form['newusername']
        user.password = request.form['newpassword']
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('account.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html.html')
    username = request.form['username']
    password = request.form['password']
    registered_user = User.query.filter_by(username=username,password=password).first()
    if registered_user is None:
        return 'Username or Password is invalid' , 'error'
        return redirect(url_for('login'))
    login_user(registered_user)
    if username=='admin' and password=='admin':
       return redirect(url_for('admin'))
    redirect_url = request.args.get('next') or url_for('dash')
    return redirect(redirect_url)

@app.route('/dash', methods=['GET','POST'])        
@login_required
def dash():
           return render_template("dash.html")

@app.route('/statistics', methods=['GET','POST'])     
@login_required
def statistics():
           return render_template("statistics.html")

@app.route('/logout', methods=['GET','POST'])
def logout():
  logout_user()
  return render_template("welcome.html")

@app.route('/admin', methods=['GET','POST'])     
def admin():
           return render_template("dashadmin.html")

@app.route('/admin/nodes', methods=['GET','POST'])     
def nodes():
           return render_template("nodes.html")

@app.before_request
def log_request_info():
   app.logger.debug('Headers: %s', request.headers)
  #  app.logger.debug('Body: %s', request.get_data())

#import logging
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)

if __name__ == '__main__':
    import logging
    logging.basicConfig(filename='error.log',level=logging.DEBUG)
    app.run('0.0.0.0', 8080)
