#let us start with a basic ml app using flask

from flask import Flask, render_template,request
import numpy as np
app = Flask(__name__)

#loading the model
import pickle
model=pickle.load(open(r"App\model.pkl","rb"))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/output',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        slength=int(request.form.get['a'])
        swidth=int(request.form.get['b'])
        plength=int(request.form['c'])
        pwidth=int(request.form.get['d'])
        data=np.array([[slength,swidth,plength,pwidth]])
        yhat=model.predict(data)
        return render_template('output.html',prediction=yhat)
    else:
        return "<h1>Failed to initialize</h1>"

if __name__=='__main__':
    app.run(debug=True,port=5002)

