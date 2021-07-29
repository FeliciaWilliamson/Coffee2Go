"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime
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
        message='Your application description page.',
        year=datetime.now().year
    )
#route for login page
@route('/login')
@view('login')
def login():
    """Renders the login page."""
    return dict(
        title = 'Login',
        message= 'Please Login Below',
        year=datetime.now().year
        )
#route for new user page
@route('/newUser')
@view('newUser')
def newUser():
    """Renders the new user page."""
    return dict(
        title = 'New User',
        message= 'Please Sign Up ',
        year=datetime.now().year
        )
#This is the route for the map page taht we have not created yet
@route('/map')
@view('map')
def map():
    """Renders the map page."""
    return dict(
        title = 'Coffee Fix',
        message= 'Please Sign Up ',
        year=datetime.now().year
        )
#route for the image 
@route('/static/<filename:path>', name='static')
def serve_static(filename):
    return static_file(filename, root='static')