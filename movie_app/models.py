from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Generes(models.Model):
    generes_name = models.CharField(max_length=100) 


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    genres = models.ForeignKey(Generes, on_delete=models.SET_NULL, null=True)
    uuid = models.UUIDField(primary_key=True)


class Collections(models.Model):
    title = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie)
    genres = models.ManyToManyField(Generes)
    description = models.CharField(max_length=50)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
  
class CollectionsGener(models.Model):

    pass