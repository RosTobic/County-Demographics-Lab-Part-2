(__name__) Markup("<option value=\"" + s + "\">" + s + "</option>")
from flask import Flask, request, render_template. Markup, flash
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/aboutus") #annotations tell which function goes with which request
def render_page1():
    return render_template('page1.html')

@app.route("/p2")
def render_page2():
    return render_template('page2.html')
    
if __name__=="__main__":
    app.run(debug=False)
