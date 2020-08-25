# coding=utf-8
from flask import Flask, jsonify, render_template, request
from flask_restful import Api
from db import db

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/anschlussquali'
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'Bernmobil'
api = Api(app)
db.init_app(app)



@app.route("/")
def hello():
    return render_template("start.html")

@app.route("/auswahl")
def auswahl():
    return render_template("auswahl.html")

@app.route('/resultat')
def resultat():
    return render_template("resultat.html")

 
@app.route('/liste')
def zeigeliste():
    return render_template("liste.html")

@app.route('/testwtf')
def test():
    return render_template("testwtf.html")

# Damit wird das Ganze gestartet.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

    