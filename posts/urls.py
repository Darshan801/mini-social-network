from django.contrib import admin
from django.urls import path,include
from posts import views

urlpatterns = [
    path('post/',views.post,name='post')
]
