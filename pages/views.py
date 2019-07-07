from django.shortcuts import render, redirect
import random
from questions.models import Question
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from config import *
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('./firekey.json')
if not len(firebase_admin._apps):
    firebase_admin.initialize_app(cred)
db = firestore.client()

total_questions_mcq = totalQuestions
total_questions_db = Question.objects.count()


# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def loggedin_view(request, *args, **kwargs):
    request.session['questions'] = []
    request.session['questions'].clear()
    request.session['questions'].append(total_questions_mcq)
    for i in range(1, total_questions_mcq + 1, 1):
        request.session['questions'].append(random.randrange(1, total_questions_db + 1, 1))
    request.session['score'] = 0
    return render(request, "loggedin.html", {'first': request.session['questions'][1]})


def questions_view(request, index=-1):  # if random function is used in url it always return 2

    if index == -1:
        index = random.randrange(1, total_questions_db + 1, 1)
    obj = Question.objects.get(id=request.session['questions'][index])
    context = {

        'event': eventName,
        'object': obj,
        'total_questions_mcq': total_questions_mcq,
        'total_questions_db': total_questions_db,
        'id_array': request.session['questions'],
        'index': index
    }

    return render(request, "questions.html", context);


def loggedout_view(request, *args, **kwargs):
    return render(request, "loggedout.html", {})


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password1')
            query = db.collection("cerebro").where('email', '==', email).get()
            f = 0

            for x in query:

                data = x.to_dict()
                if data['email'] == email and data['ticketno'] == pwd:
                    f = 1
                    request.session['userid'] = x.id
                    name = data['name']

            if f == 1:
                print("Firestore Successful")
                # user = form.save()
                user = User.objects.create_user(name, email, pwd)
                user.save()
                login(request, user)
                messages.info(request, f"You are now logged in as: {name}")

                return redirect("loggedin")
            else:
                messages.error(request, "Invalid username or password")
                print("Invalid username or password")
        else:
            print("Invalid form")
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            # print(form.error_messages[msg])
    form = UserCreationForm
    context = {
        "form": form
    }
    return render(request, "register.html", context)


def logout_request(request):
    logout(request)
    messages.info(request, "Bye!")
    return redirect("home")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
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
    return render(request, "home.html", {"form": form})
