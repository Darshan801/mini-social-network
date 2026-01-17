from django.contrib import admin
from django.urls import path,include
from posts import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    #path('post/',views.post,name='post'),
    path('createpost/',views.createpost,name='createpost'),
    path('likepost/',views.likepost,name='likepost'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
