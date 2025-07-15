from flask import Flask, render_template, url_for, redirect


app= Flask (__name__)

@app.route('/')

@app.route('/index', methods=['GET','POST'])
def index():
    return render_template('index.html')
    
