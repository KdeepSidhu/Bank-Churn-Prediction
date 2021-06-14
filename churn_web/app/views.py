from django import http
from django.shortcuts import render
import numpy as np
import pickle
import os

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
static = os.path.join(BASE_DIR, "static")

def home(request):
    if request.method =='POST':
        one = request.POST['1']
        two = request.POST['2']
        three = request.POST['3']
        four = request.POST['4']
        five = request.POST['5']
        six = request.POST['6']
        seven = request.POST['7']
        eight = request.POST['8']
        nine = request.POST['9']
        ten = request.POST['10']
        feature = [one,two,three,four,five,six,seven,eight,nine,ten]
        feature = np.array(feature)
        feature = feature.reshape(1,10)
        scaler = pickle.load(open(static+'/scaler.sav','rb'))
        feature = scaler.transform(feature)
        model = pickle.load(open(static+'/XGB_model.sav','rb'))
        pred =  model.predict(feature)
        print(pred)
        context = {
            'output': pred[0]
        }
        return(render(request,'home1.html',context))
    return(render(request,'home1.html'))

