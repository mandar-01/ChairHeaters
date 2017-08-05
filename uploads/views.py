from django.shortcuts import render


# Create your views here.
def upload_view(request):
	return render(request,'index.html',{})
