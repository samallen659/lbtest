from flask import Flask, render_template
import platform

app = Flask(__name__)

@app.route("/")
def home():
    hostname = platform.node()
    return render_template("index.html", hostname=hostname)
