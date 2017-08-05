from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
class upload(models.Model):
	username = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	docFile = models.FileField(default='settings.MEDIA_ROOT/dbms.pdf')

	def __unicode__(self):
		return self.title
