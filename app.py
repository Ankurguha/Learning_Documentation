from flask import Flask,render_template,url_for,request,redirect
import pandas as pd
import numpy as np
app=Flask(__name__)


Indication_info={}
@app.route('/')
def home():
    return render_template('home.html')


if __name__=='__main__':
    app.run(debug=True)