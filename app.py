# coding=utf-8
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    items = ["Apfel", "Birne", "Banane"]

    return render_template("start.html", name="Max Mustermann", items=items)

@app.route("/test")
def f123467890():
    paragraph = "<p>Hallo Welt</p>"
    return "Hello Test!" + paragraph

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
