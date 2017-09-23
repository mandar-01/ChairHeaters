from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.text import slugify

# Create your models here.
class upload(models.Model):
	#username = models.CharField(max_length=100)
	user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=300,default=None)
	#content = models.TextField(default=None,blank=True,null=True)
	docFile = models.FileField(default=None,blank=True,null=True)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ["-timestamp"]

	def get_absolute_url(self):
		return reverse("detail",kwargs={"id":self.id})

"""
def create_slug(instance,new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = upload.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = slug = "%s-%s" %(slug,qs.first().id)
		return create_slug(instance,new_slug=new_slug)
	return slug

def pre_save_upload_receiver(sender,instance,*args,**kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)



pre_save.connect(pre_save_upload_receiver,sender=upload)
"""