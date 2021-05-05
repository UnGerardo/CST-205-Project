from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/', methods=["GET"])
def home():
    return render_template("index.html")
    
