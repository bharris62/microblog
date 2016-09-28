from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'bharris62'}  # fake user
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Sun Drop is the best drink ever!'
        },
        {
            'author': {'nickname': 'Jane'},
            'body': 'Worst. Movie. Ever!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)