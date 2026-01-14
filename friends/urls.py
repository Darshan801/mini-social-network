from django.urls import path
from . import views

app_name = 'friends'  # important for namespace

urlpatterns = [
    path('', views.friends_home, name='home'),
]