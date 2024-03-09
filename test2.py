from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("index.html", icerik=["elma", "armut", "muz"])

if __name__ == "__main__":
    app.run()

#return render_template("index.html", icerik=name, r=2)