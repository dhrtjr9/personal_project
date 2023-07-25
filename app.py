from flask import Flask, render_template, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from import models
import config

db = SQLAlchemy()
Migrate = Migrate()

app = Flask(__name__)
app.config.from_object(config)

#orm
db.init_app(app)
Migrate.init_app(app, db)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/about')
def about():
    return "about World!"

@app.route('/cart')
def cart():
    return render_template("cart.html")

@app.route('/login')
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


@app.route('/html_test')
def hello_html():
    # html file은 templates 폴더에 위치해야 함
    return render_template('login_rawtest.html')

if __name__ == '__main__':
    app.run()