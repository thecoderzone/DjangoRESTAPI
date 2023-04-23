from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class todo(models.Model):
     """ Models for a todo List"""
     task = models.CharField(max_length=150)
     timestamp = models.DateField(auto_now_add = True, auto_now = False, blank = True)
     completed = models.BooleanField(default = False, blank = True)
     updated = models.DateTimeField(auto_now = True, blank = True)
     user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
     
     def __str__(self):
          """returning a string"""
          
          return self.task