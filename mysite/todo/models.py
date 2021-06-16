from django.db import models
import datetime
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# class CreateUser(models.Model):
# 	user = models.ForeignKey(User,max_length=40)
# 	def __str__(self):
# 		return self.user

class Todo(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	text = models.CharField(max_length=70)
	created_date = models.DateTimeField(default=datetime.datetime.now) 
	complete= models.BooleanField(default=False)
	def __str__(self):
		return self.text
