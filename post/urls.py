from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^posts/$', views.PostsList.as_view({'get': 'list'}), name='posts-list'),
]