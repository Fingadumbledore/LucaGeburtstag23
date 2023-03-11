""" Flask app for the application. """

import os
import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,
            template_folder='sites',
            static_folder='static')
DEBUG=True
BACKUP=os.getenv('BACKUP')
WORT_ANZAHL = 12

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
    # ab hier wenn kein backup in kraft
    
    # hard coded wort länge lol
    wort_laengen = [
            4,
            11,
            3,
            4,
            2,
            4,
            12,
            4,
            10,
            6,
            3,
            3
    ]

    # das muss gemacht werden, weil flask lost ist.
    # request.form.items() ist ein Iterator[tuple[str, str]], keine List[tuple[str, str]]. deswegen muss das so gemacht werden.
    # man kann halt nicht in einen Iterator indexen, weil er halt durchlaufen werden muss und das nur ein mal kann.
    request_items = [(key, val) for (key, val) in request.form.items()]

    def get_offset(i):
        w = 0
        for i in range(i):
            w += wort_laengen[i]
        return w

    antw = []

    for i in range(WORT_ANZAHL):
        wort_l = wort_laengen[i]
        wort_offset = get_offset(i)
        # magie mit sogenannten list comprehensions um so genannte slices zu kriegen
        wort_in_array_ding = request_items[wort_offset:wort_offset+wort_l]
        # die slice ist halt ein array ne..., also muss gejoined werden
        wort = ''.join([val for (_, val) in wort_in_array_ding]).lower()
        antw.append(wort)
            
    false_awnsers = validate(antw)
    if not false_awnsers:
        return redirect(url_for('karte'))
    text = 'falsch sind: ' + str(false_awnsers)
    
    return render_template('raetsel.html', falsch_text=text)


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
                false_awnsers.append(i+1)
    return false_awnsers


if __name__ == '__main__':
    app.run(debug=DEBUG)
