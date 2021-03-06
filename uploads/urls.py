"""chairheaters URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.upload_view),
    url(r'^list/$', views.post_list,name='list'),
    url(r'^(?P<id>\d+)/$', views.post_detail,name="detail"),
    url(r'^(?P<id>\d+)/edit/$', views.update_post,name="update"),
    url(r'^(?P<id>\d+)/delete/$', views.delete_post),
    url(r'^create/$',views.create_post),
    url(r'^myposts/$',views.my_posts),
]
