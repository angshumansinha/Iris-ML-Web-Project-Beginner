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

@app.route('/output',methods=['POST'])
def predict():
    if request.method=='POST':
        slength=int(request.form['a'])
        swidth=int(request.form['b'])
        plength=int(request.form['c'])
        pwidth=int(request.form['d'])
        data=np.array([[slength,swidth,plength,pwidth]])
        yhat=model.predict(data)
        return render_template('output.html',data=yhat)


if __name__=='__main__':
    app.run(debug=True)

