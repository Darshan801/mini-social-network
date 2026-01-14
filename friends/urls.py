from django.urls import path
from . import views

app_name = 'friends'

urlpatterns = [
    path('', views.friends_list, name='list'),
    path('send/<int:user_id>/', views.send_friend_request, name='send_request'),
    path('requests/', views.friend_requests, name='requests'),
    path('accept/<int:request_id>/', views.accept_request, name='accept'),
    path('reject/<int:request_id>/', views.reject_request, name='reject'),
]

