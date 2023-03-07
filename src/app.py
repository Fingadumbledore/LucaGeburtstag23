""" Flask app for the application. """

import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,
            template_folder='sites',
            static_folder='static')
DEBUG=True

@app.route('/')
def index():
    """ Render the index page. """
    return render_template('index.html')

@app.route('/caeser')
def caeser():
    """ Render the caeser page. """
    return render_template('caeser.html')

@app.route('/hilfe')
def hilfe():
    return render_template('hilfe.html')

@app.route('/raetsel')
def raetsel():
    return render_template('raetsel.html')

@app.route('/luftpumpe')
def luftpumpe():
    return render_template('luftpumpe.html')

@app.route('/player')
def player():
    return render_template('player.html')

@app.route('/karte')
def karte():
    return render_template('karte.html')

@app.route('/videos')
def videos():
    return render_template('videos.html')

@app.route('/werkzeugkoffer')
def wekzeugkoffer():
   return render_template('werkzeugkoffer.html')

@app.route('/fragen_abschicken', methods=['POST'])
def fragen_abschicken():
    buchstabe = request.form['buchstabe']
    wort = request.form['wort']
    kästchen = request.form['kaestchen']

    return redirect('/raetsel')


if __name__ == '__main__':
    app.run(debug=DEBUG)
