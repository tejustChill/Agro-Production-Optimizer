from flask import Flask, render_template, request
app = Flask(__name__)

#for data manipulations
import numpy as np
import pandas as pd     
import joblib

model = joblib.load('crop_app_model.pkl')

@app.route("/", methods=["GET"])
def home():
     return render_template('index.html')


@app.route('/', methods=['POST'])
def getInput():
    n = float(request.form['nitro'])
    p = float(request.form['phos'])
    k = float(request.form['pota'])
    temp = float(request.form['temp'])
    hum = float(request.form['hum'])
    ph = float(request.form['ph'])
    rain = float(request.form['rain'])
    prediction = model.predict(np.array([[n, p, k, temp, hum, ph, rain]]))
    imageList={}
    for i in prediction:
     if i=='mango':
          imageList={'Mango':'../static/images/mango.jpg'}
     if i=='rice':
          imageList={'Rice':'../static/images/rice.jpg'}
     if i=='pomegranate':
          imageList={'Pomegranate':'../static/images/pomegranate.jpg'}
     if i=='pigeonpeas':
          imageList={'Pigeonpeas':'../static/images/pigeonpeas.jpeg'}
     if i=='papaya':
          imageList={'Papaya':'../static/images/papaya.jpg'}
     if i=='orange':
          imageList={'Orange':'../static/images/orange.jpg'}
     if i=='muskmelon':
          imageList={'Muskmelon':'../static/images/muskmelon.jpeg'}
     if i=='mungbean':
          imageList={'Mungbean':'../static/images/mungbeans.jpg'}
     if i=='mothbeans':
          imageList={'Mothbean':'../static/images/mothbean.jpeg'}
     if i=='lentil':
          imageList={'Letil':'../static/images/lentil.jpg'}
     if i=='kidneybeans':
          imageList={'Kidneybeans':'../static/images/kidneybean.jpeg'}
     if i=='grapes':
          imageList={'Grapes':'../static/images/grapes.jpeg'}
     if i=='jute':
          imageList={'Jute':'../static/images/jute.jpg'}
     if i=='blackgram':
          imageList={'Blackgram':'../static/images/blackgram.jpg'}
     if i=='apple':
          imageList={'Apple':'../static/images/apple2.jpeg'}
     if i=='coffee':
          imageList={'Coffee':'../static/images/coffee.jpeg'}
     if i=='maize':
          imageList={'Maize':'../static/images/maize.png'}
     if i=='watermelon':
          imageList={'Watermelon':'../static/images/watermelon.jpeg'}
     if i=='banana':
          imageList={'Banana':'../static/images/banana.jpeg'}
     if i=='coconut':
          imageList={'Coconut':'../static/images/coconut.jpg'}
     if i=='cotton':
          imageList={'Cotton':'../static/images/cotton.jpeg'}
     if i=='chickpea':
          imageList={'Chickpea':'../static/images/chickpea.jpg'}

    #return prediction
    return render_template('index.html', res=imageList)