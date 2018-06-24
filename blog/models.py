from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin
from keras.preprocessing.sequence import skipgrams
from keras.preprocessing.text import hashing_trick


class Comment(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()



    def __str__(self):
        return self.title

