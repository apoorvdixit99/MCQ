import firebase_admin
from django.shortcuts import render
from django.http import HttpResponse
from questions.models import Question
import json
import firebase_admin as firebase
from firebase_admin import credentials, firestore
from config import *

cred = credentials.Certificate('./firekey.json')
db = firestore.client()




# Create your views here.

def submit_data(request):
    ansdict = json.loads(str(request.POST['answers']))
    print(str(ansdict))

    for i in ansdict:
        if Question.objects.get(id=i).correct_option.upper() == ansdict[i]:
            request.session['score'] += marksCorrect
        

    db.collection("cerebro").document(request.session['userid']).update({'score': request.session['score']})
    print(request.session['score'])
    return HttpResponse("Your Score is " + str(request.session['score']))
