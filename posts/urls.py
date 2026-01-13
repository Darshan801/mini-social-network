from django.contrib import admin
from django.urls import path,include
from posts import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('post/',views.post,name='post')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
