# coding=utf-8
from flask import Flask, render_template, request, url_for
from netz2 import anschluss

app = Flask(__name__)

class Item():
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

@app.route("/")
def hello():
    items = [
        Item("Apfel", 5),
        Item("Computer", 1),
        Item("Birne", 4)
    ]

    person = ("Hans", "Zimmermann")

    return render_template("start.html", person=person, items=items)

@app.route("/test")
def f123467890():
    name = request.args.get("name")
    age = request.args.get("age")
    return render_template("test.html", name=name, age=age)

@app.route("/currency")

def waerungsrechner():
    d = {
        "EUR": 1.06,
        "GPB": 0.85
    }

    chf = request.args.get("chf", 1)
    chf = float(chf)
    eur = round(chf * d.get("EUR"), 2)
    gpb = round(chf * d.get("GPB"), 2)    
    
    return render_template("currency.html", chf=chf, eur=eur, gpb=gpb)


@app.route("/auswahl", methods=['GET', 'POST'])
def anschlussauswahl():
    if request.method == 'POST':
        auswahl = request.form.getlist("anschluss")
        for item in auswahl:
            resultat = anschluss(item)
            legend = 'Auswertung xxx'
            labels = item
            total_anschluesse = len(resultat)
            OK_anschluesse = 21 # ACHTUNG Wert noch berechnen!!!!!!
            values = total_anschluesse
            return render_template("resultat.html", values=values, labels=labels, legend=legend)
    return render_template("auswahl.html")

@app.route('/resultat')
def anschlussresultat(resultat):
    pass
    return render_template("resultat.html")


@app.route('/liste')
def zeigeliste():
    pass
    return render_template("liste.html")

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
