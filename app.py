from flask import Flask, url_for
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/addnewemployee')
def addnewemployee():
    return render_template('addnewemployee.html')

@app.route('/singleemployeeprofile')
def singleemployeeprofile():
    return render_template('singleemployeeprofile.html')

@app.route('/updateemployee')
def updateemployee():
    return render_template('updateemployee.html')


def logout():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)