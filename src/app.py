""" Flask app for the application. """

import os
import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,
            template_folder='sites',
            static_folder='static')
DEBUG=True
BACKUP=os.getenv('BACKUP')

@app.route('/')
def index():
    """ Render the index page. """
    return render_template('index.html')

@app.route('/hilfe')
def hilfe():
    return render_template('hilfe.html')

@app.route('/raetsel')
def raetsel():
    print(os.getenv('BACKUP'))
    if BACKUP is not None:
        return render_template('backup_raetsel.html')
    return render_template('raetsel.html')

@app.route('/player')
def player():
    return render_template('player.html')

@app.route('/karte')
def karte():
    return render_template('karte.html')

@app.route('/videos')
def videos():
    return render_template('videos.html')

@app.route('/fragen_abschicken', methods=['POST'])
def fragen_abschicken():
    if BACKUP is not None:
        awnsers = []
        for i in range(12):
            awnsers.append(request.form[str(i+1)])

        false_awnsers = validate(awnsers)
        if false_awnsers:
            return redirect(url_for('raetsel', false_awnsers=false_awnsers))
        return redirect(url_for('karte'))

    buchstabe = request.form['buchstabe']
    wort = request.form['wort']
    kästchen = request.form['kaestchen']
    return redirect('/raetsel')

# return list of indexes, where awnser ist false
def validate(awnsers) -> list[int]:
    """ Validate the awnsers. """
    false_awnsers = []
    with open('data/fragen.json') as file:
        data = json.load(file)
        # enumeriert die liste und schaut ob die antworten stimmen
        for i, awnser in enumerate(awnsers):
            # wenn die antwort nicht in den antworten ist dann füge die index in die liste, in kann man auch so verwenden lol...
            # https://www.digitalocean.com/community/tutorials/python-find-string-in-list krass
            if awnser not in data[i]['antworten']:
                print(awnser)
                false_awnsers.append(i)
    return false_awnsers


if __name__ == '__main__':
    app.run(debug=DEBUG)
