"""
Routes and views for the bottle application.
"""

from bottle import route, view,get, post, request, redirect, template 
from datetime import datetime
import re
#route for home page
@route('/')
@route('/home')
@view('index')

def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

#route for about page
@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='A little about us.',
        year=datetime.now().year
    )

   
#route for login page
@route('/login', method=['GET','POST'])
@view('login')
def login():

    return dict(
       title= 'Login',
       year=datetime.now().year,
       message= "Please login"
  )
#Code below is suppposed to be a test for if the user input is blank or not and the password is the correct combination.
@route('/error', method=['GET','POST'])
def validate():
    while True:
        username= request.params.get('userName')
        password=request.params.get('password')
        if (len(password) < 8) and (username == ""):
            return template('error.html', "Make sure your password is at lest 8 letters")
        elif (re.search('[0-9]',password ) is None) and (username == ""):
            return template('error.html', "Make sure your password has a number in it")      
        elif (re.search('[A-Z]',password) is None) and (username == ""): 
            return template('error.html', "Make sure your password has a capital letter in it")
        else:
            return template("map.html")
            


#route for new user page
@route('/newUser',method=['GET','POST'])
@view('newUser')
def newUser():
    """Renders the new user page."""
    return dict(
        title = 'New User',
        message= 'Please Sign Up ',
        year=datetime.now().year
        )

#This is the route for the map page 
@route('/map')
@view('map')
def map():
    """Renders the map page."""
    return dict(
       title = 'Coffee Fix',
        year=datetime.now().year
        )
#route for the image 
@route('/static/<filename:path>', name='static')
def serve_static(filename):
    return static_file(filename, root='static')