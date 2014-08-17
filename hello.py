

import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #return 'Site Down For Maintenance'
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html')

if __name__=='__main__':
    app.run()
