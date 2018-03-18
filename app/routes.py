from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
  user = {'username' : 'Ginga', 'password' : '12345safe'}
  return render_template('index.html', title="whatever", user=user)

@app.route('/register')
def register():
  return render_template('register.html', msg="do et now")