from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

# Create your models here.
class upload(models.Model):
	username = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=300,default=None)
	docFile = models.FileField(default=None,blank=True)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ["-timestamp"]

	def get_absolute_url(self):
		return reverse("detail",kwargs={"id":self.id})
