from django.db import models

from django.contrib.auth.models import User

class Page(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now=True)
	content = models.TextField()
	title = models.TextField()
