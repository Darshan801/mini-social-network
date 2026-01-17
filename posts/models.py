from django.db import models
from django.contrib.auth import get_user_model
import datetime
from django.utils import timezone

User = get_user_model()

class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='images/images', default='')
    profile_bio = models.TextField(max_length=50)
    location= models.CharField(max_length=100,blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    like=models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    


class Likepost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username