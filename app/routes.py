from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
  user = {'username' : 'Ginga', 'password' : '12345safe'}
  return render_template('index.html', title="whatever", user=user)