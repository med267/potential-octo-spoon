from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
  user = {'username': 'Jeff'}

  posts = [
    {
      'author': {'username': 'John'},
      'body': 'Beautiful Day In Krasnodar!',
      'caloriesforday': 1389
    },
    {
      'author': {'username': 'Susan'},
      'body': 'The Avengers was great!',
      'caloriesforday': 600
    }
  ]
  return render_template('index.html', title='Monkeybear', user=user, posts=posts)
