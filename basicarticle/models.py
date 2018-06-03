# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
	
	#author = models.ForeignKey(User, unique=True)
	author = models.CharField(max_length = 64)
	
	title = models.CharField(max_length = 64)
	
	content = models.TextField(max_length = 16384)
	
	votes = models.IntegerField(default=0)

