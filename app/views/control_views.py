
from flask import Blueprint, request, render_template, flash, url_for, session, g
from app.models import User
from app import db
import functools

test = Blueprint('test', __name__, url_prefix='/')

@test.route('/')
def hello():
    user  = User()
    return render_template("index.html")

@test.route('/about')
def about():
    return "about World!"

@test.route('/cart')
def cart():
    return render_template("cart.html")

@test.route('/login')
def login():
    email_address = request.args.get('email_address')
    passwd = request.args.get('passwd')
    print(email_address, passwd)

    # if email_address == 'dave@gmail.com' and passwd == '111':

    #     return_data = {'auth': 'success'}
    # else:
    #     return_data = {'auth': 'failed'}
    # return jsonify(return_data)
    return render_template("login_rawtest.html")


@test.route('/html_test')
def hello_html():
    # html file은 templates 폴더에 위치해야 함
    return render_template('login_rawtest.html')
