# coding=utf-8
from flask import Flask, render_template, request, url_for
from work import Anschlussdaten, anschluss_2870, anschluss_1260

app = Flask(__name__)

class Item():
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class Datensatz():
    def __init__(self, zubringer, abbringer, anschluss):
        self.zubringer = zubringer
        self.abbringer = abbringer
        self.anschluss = anschluss

    def ausgabe(self):
        (print(self.anschluss_name, self.zubringer, self.abbringer, self.anschluss))


class Resultat():
    def __init__(self):
        self.resultat_anschluss = []

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
        for nummer in auswahl:
            nummer = Anschlussdaten(nummer)
            nummer.anschluss(nummer)

    return render_template("auswahl.html")

@app.route('/resultat')



#def anschlussresultat(self):
#    self.master_lesen()
#    for key in self.__master_output:
#        print(key)
    #    total_anschluesse = resultat[0] + resultat[1]
    #    print(total_anschluesse)
    #    OK_anschluesse = resultat[0]
    #    print(OK_anschluesse)
    #    values = int(OK_anschluesse) / int(total_anschluesse) * 100
    #    legend = 'Auswertung xxx'
    #    labels = nummer
#        return render_template("resultat.html")


 
@app.route('/liste')
def zeigeliste():
    pass
    return render_template("liste.html")

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
