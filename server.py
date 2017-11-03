from flask import Flask, render_template,request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "secret"

@app.before_first_request
def setup():
    session['key'] = random.randrange(0,101)
    session['comment'] = "Too High!"

@app.route('/')
def index():
    print session['key']
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    if str(session['key'])==request.form['guess']:
        return redirect('/winner')
    if str(session['key'])<request.form['guess']:
        session['comment'] = "Too high!"
        return redirect('/try')
    if str(session['key'])>request.form['guess']:
        session['comment'] = "Too low!"
        return redirect('/try')

@app.route('/try')
def tryA():
    return render_template('tryAgain.html')

@app.route('/winner')
def winner():
    return render_template('winner.html')

@app.route('/reset')
def reset():
    print "Hit Route"
    session.pop('key')
    session['key'] = random.randrange(0,101)
    print session['key']
    return redirect('/')
        
    
app.run(debug=True)