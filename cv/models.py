from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Education(models.Model):
    university = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    graduation = models.CharField(max_length=200)
    description = models.TextField(blank=True)

class Project(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    languages = models.CharField(max_length=200)
    repository = models.CharField(max_length=200,blank=True)
    description = models.TextField(blank=True)

class Experience(models.Model):
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    description = models.TextField(blank=True)

class Certificate(models.Model):
    name = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    company = models.CharField(max_length=200)

class Skill(models.Model):
    topic = models.CharField(max_length=200)
    skill = models.TextField()
