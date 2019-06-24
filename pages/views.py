from django.shortcuts import render
import random 
from questions.models import Question

# Create your views here.
def home_view(request,*args, **kwargs):
	return render(request, "home.html", {})
	
def loggedin_view(request,*args, **kwargs):
	return render(request, "loggedin.html", {})

def questions_view(request,*args, **kwargs):
	num = random.randrange(1,5,1)
	obj = Question.objects.get(id=num)
	context = {
		'object' : obj
	}
	return render(request,"questions.html",context);
	
def loggedout_view(request,*args, **kwargs):
	return render(request, "loggedout.html", {})
