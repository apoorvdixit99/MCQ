from django.db import models

# Create your models here.


class Scores(models.Model):
    username = models.TextField()
    event = models.TextField()
    score = models.IntegerField()
