from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                           title='Sign In',
                           form=form)