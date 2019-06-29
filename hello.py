import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mcq.settings")
import django
django.setup()
from questions.models import Question
import random


for i in range(50):
    name= str(random.randrange(3000,4000)) + "dfsdfgsdgsg"
    opt_a = str(random.randrange(3000, 4000)) + "sgsgfsgsdgsg"
    opt_b = str(random.randrange(3000, 4000)) + "sgsgfsgsdgsg"
    opt_c = str(random.randrange(3000, 4000)) + "sgsgfsgsdgsg"
    opt_d = str(random.randrange(3000, 4000)) + "sgsgfsgsdgsg"
    Question.objects.create(problem=name, option_a=opt_a, option_b=opt_b,
                            option_c=opt_c, option_d=opt_a, correct_option="a")

