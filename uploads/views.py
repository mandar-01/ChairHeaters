from django.shortcuts import render,get_object_or_404,redirect
from uploads.models import upload
from django.http import HttpResponseRedirect,Http404
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect



# Create your views here.
def upload_view(request):
	return render(request,'base.html',context)

@login_required
def post_list(request):
	queryset_list = upload.objects.all() # Get all database querysets
	queryset = upload.objects.all()

	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
			).distinct()

	paginator = Paginator(queryset_list, 2) # Show 2 contacts per page

	page = request.GET.get('page')
	try:
	    queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)
	context = {"object_list" : queryset}
	return render(request,'post_list.html',context)

def post_detail(request,id=None):
	instance = get_object_or_404(upload,id=id)
	context = {"title":instance.title,"instance":instance}
	return render(request,"post_detail.html",context)

@login_required
def create_post(request):
	# if not request.user.is_staff or not request.user.is_superuser:
	# 	raise Http404
	form = PostForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	  "form" : form
	}
	return render(request,'form.html',context)

def delete_post(request,id=None):
	instance = get_object_or_404(upload,id=id)
	if instance.user == request.user:
		instance.delete()
		return redirect('/uploads/list/')
	else:
		return render(request,"cantdel.html",{"title" : "delete"})

def update_post(request,id=None):
	instance = get_object_or_404(upload,id=id)
	if instance.user == request.user:
		form = PostForm(request.POST or None,instance=instance)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return HttpResponseRedirect(instance.get_absolute_url())
	else:
		return render(request,"cantdel.html",{"title" : "update"})

	context = {
	  "title" : instance.title,
	  "form" : form,
	  "instance" : instance,
	}
	return render(request,'form.html',context)
def my_posts(request):
	queryset_list = upload.objects.filter(user=request.user) # Get all database querysets
	queryset = upload.objects.all()

	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
			).distinct()

	paginator = Paginator(queryset_list, 2) # Show 2 contacts per page

	page = request.GET.get('page')
	try:
	    queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)
	context = {"object_list" : queryset}
	return render(request,'post_list.html',context)
