import firebase_admin
from django.shortcuts import render
from django.http import HttpResponse
from questions.models import Question
import json
import firebase_admin as firebase
from firebase_admin import credentials, firestore
from config import *
from django.contrib.auth import logout

cred = credentials.Certificate('./firekey.json')
db = firestore.client()




# Create your views here.

def submit_data(request):
    ansdict = json.loads(str(request.POST['answers']))
    print(str(ansdict))

    for i in ansdict:
        if Question.objects.get(id=i).correct_option.upper() == ansdict[i]:
            request.session['score'] += marksCorrect
            print('id:'+i+':'+Question.objects.get(id=i).correct_option.upper())
        else:
                 request.session['score'] -= marksIncorrect


        

    db.collection("cerebro").document(request.session['userid']).update({'score': request.session['score']})
    print(request.session['score'])
    score = request.session['score']
    logout(request)
    return HttpResponse("Your Score is " + str(score))

