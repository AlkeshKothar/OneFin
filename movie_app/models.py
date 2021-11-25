from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Collections(models.Model):
    collection_name = models.CharField(max_length=100)
    movie = models.CharField(max_length=50)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    
