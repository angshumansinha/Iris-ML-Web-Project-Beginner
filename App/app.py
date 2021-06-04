#let us start with a basic ml app using flask

from flask import Flask, render_template,request
from flask_cors import cross_origin
import numpy as np
app = Flask(__name__)

#loading the model
import pickle
model=pickle.load(open(r'App\model.pkl',"rb"))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
@cross_origin()
def predict():
    if request.method=='POST':
        slength=int(request.form['a'])
        swidth=int(request.form['b'])
        plength=int(request.form['c'])
        pwidth=int(request.form['d'])
        yhat=model.predict([[slength,swidth,plength,pwidth]])
        return render_template('output.html',prediction=yhat[0])

if __name__=='__main__':
    app.run(debug=True)

