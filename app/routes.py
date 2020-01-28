from app import app

@app.route('/')
@app.route('/index')
def index():
  user = {'username': 'Jeff'}
  return '''
<html>
  <head>
      <title>CountIt</title>
  </head>
  <body>
    <h1> Hello, ''' + user['username'] + '''!</h1>
  </body>
</html>
'''
