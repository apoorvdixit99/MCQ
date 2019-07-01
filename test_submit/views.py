import firebase_admin
from django.shortcuts import render
from django.http import HttpResponse
from questions.models import Question
import json
import firebase_admin as firebase
from firebase_admin import credentials, firestore

cred = credentials.Certificate('./firekey.json')
db = firestore.client()

score = 0


# Create your views here.

def submit_data(request):
    ansdict = json.loads(str(request.POST['answers']))
    print(str(ansdict))
    global score
    for i in ansdict:
        if Question.objects.get(id=i).correct_option.upper() == ansdict[i]:
            score += 1
    db.collection("cerebro").document(request.session['userid']).update({'score': score})
    print(score)
    return HttpResponse("Your Score is " + str(score))
