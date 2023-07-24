from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

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
    return render_template("login.html")

@app.route('/registerForm')
def registerForm():
    return render_template("login.registerForm.html")

if __name__ == '__main__':
    app.run()