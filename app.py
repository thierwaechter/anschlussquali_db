# coding=utf-8
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    items = ["Apfel", "Birne", "Banane"]

    return render_template("start.html", name="Max Mustermann", items=items)

@app.route("/test")
def f123467890():
    name = request.args.get("name")
    age = request.args.get("age")
    return render_template("test.html", name=name, age=age)


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
