from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
class upload(models.Model):
	username = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=300,default=None)
	docFile = models.FileField(default=None)

	def __unicode__(self):
		return self.title
