from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class RProjects(models.Model):   # Requested Projects
	title=models.CharField(max_length=200)
	desc=models.TextField()
	timestamp=models.DateTimeField(auto_now_add=True)
	youtubelink=models.URLField(max_length=2000)
	githublink=models.URLField(max_length=2000)
	member1name=models.CharField(max_length=60)
	member1reg=models.CharField(max_length=20)
	member2name=models.CharField(max_length=60)
	member2reg=models.CharField(max_length=20)
	member3name=models.CharField(max_length=60)
	member3reg=models.CharField(max_length=20)
	member4name=models.CharField(max_length=60)
	member4reg=models.CharField(max_length=20)
	member5name=models.CharField(max_length=60)
	member5reg=models.CharField(max_length=20)
	member6name=models.CharField(max_length=60)
	member6reg=models.CharField(max_length=20)


class Projects(models.Model):   # Approved Projects
	title=models.CharField(max_length=200)
	desc=models.TextField()
	timestamp=models.DateTimeField(auto_now_add=True)
	youtubelink=models.URLField(max_length=2000)
	githublink=models.URLField(max_length=2000)
	member1name=models.CharField(max_length=60)
	member1reg=models.CharField(max_length=20)
	member2name=models.CharField(max_length=60)
	member2reg=models.CharField(max_length=20)
	member3name=models.CharField(max_length=60)
	member3reg=models.CharField(max_length=20)
	member4name=models.CharField(max_length=60)
	member4reg=models.CharField(max_length=20)
	member5name=models.CharField(max_length=60)
	member5reg=models.CharField(max_length=20)
	member6name=models.CharField(max_length=60)
	member6reg=models.CharField(max_length=20)











