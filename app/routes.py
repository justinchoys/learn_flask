from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

# @app.route('/login')
# def login():
#     form = LoginForm()
#     return render_template('login.html', title='Sign In', form=form)
# this only lets user enter data (no processing submitted data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): #this method is set to False after GET request is completed to display form
    #when browser sends POST request after user presses submits, this method will turn True if data is valid and can be processed by the application
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data)) #make sure that html file is set to handle flash messages
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)