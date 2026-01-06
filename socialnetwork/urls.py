
from django.urls import path
from socialnetwork import views

urlpatterns = [
    path('', views.home,name='home'),
]
