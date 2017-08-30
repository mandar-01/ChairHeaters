from django.shortcuts import render
from uploads.models import upload
from django.http import HttpResponseRedirect
from .forms import PostForm


# Create your views here.
def upload_view(request):
	queryset = upload.objects.all() # Get all database querysets
	# count = upload.objects.filter().count()  # Total number of objects in DB
	# i=0
	# context = {}
	# for obj in queryset:
	# 	tup = (obj.title,obj.description,obj.username,obj.docFile)
	# 	context[i] = tup
	# 	i+=1
	# return render(request,'index.html',context)
	context = {"object_list" : queryset}
	return render(request,'base.html',context)

def create_post(request):
	form = PostForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		#return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	  "form" : form
	}
	return render(request,'form.html',context)


