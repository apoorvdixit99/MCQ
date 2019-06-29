import firebase_admin
from django.shortcuts import render, redirect
import random

from firebase_admin import credentials, firestore

from questions.models import Question
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
import pyrebase
from fireconfig import config
import firebase_admin as firebase
import json

#firebase = pyrebase.initialize_app(config)
#db = firebase.database()

cred = credentials.Certificate('./firekey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()




total_questions_mcq = 4
total_questions_db = 4

# Create your views here.
def home_view(request,*args, **kwargs):
	return render(request, "home.html", {})
	
def loggedin_view(request,*args, **kwargs):
	return render(request, "loggedin.html", {})

def questions_view(request, id_number=-1):	#if random function is used in url it always return 2
	if id_number == -1:
		id_number=random.randrange(1,total_questions_db+1,1)
	obj = Question.objects.get(id=id_number)
	context = {
		'mcq_numbers' : [1,2,3,4],		#CHANGE THIS TO SIMPLE RANGE IN ACTUAL HTML FILE
		'object' : obj,
		'total_questions_mcq' : total_questions_mcq,
		'total_questions_db' : total_questions_db
	}
	return render(request,"questions.html",context);
	
def loggedout_view(request):
	ansdict = json.loads(str(request.POST['answers']))  # This dictionary has answers of user
	print("Ans dict is " + str(ansdict)) # remove this later
	return render(request, "loggedout.html", {})

def register_view(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)

		if form.is_valid():
			username = form.cleaned_data.get('username')
			pwd = form.cleaned_data.get('password1')
			query = db.collection("cerebro").where('email', '==', username).get()
			f=0

			for x in query:

				data = x.to_dict()
				if data['email'] == username and data['ticketno'] == pwd:
					f=1

			if f==1:
				print ("Firestore Successful")
				user = form.save()
				login(request, user)
				messages.info(request, f"You are now logged in as: {username}")
				return redirect("loggedin")
			else:
				messages.error(request, "Invalid username or password")
				print ("Invalid username or password")
		else:
			print ("Invalid form")
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")
				#print(form.error_messages[msg])
	form = UserCreationForm
	context = {
		"form": form
	}
	return render(request, "register.html", context)


def logout_request(request):
	logout(request)
	messages.info(request,"Bye!")
	return redirect("home")

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request,data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as: {username}")
				return redirect("loggedin")
			else:
				messages.error(request, "Invalid username or password")
		else:
			messages.error(request, "Invalid username or password")
	form = AuthenticationForm()
	return render(request, "home.html",{"form":form})