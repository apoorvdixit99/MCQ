from django.db import models

# Create your models here.

class Question(models.Model):
	problem = models.TextField()
	option_a = models.TextField()
	option_b = models.TextField()
	option_c = models.TextField()
	option_d = models.TextField()
	correct_option = models.CharField(max_length=1,blank=False,null=False)
