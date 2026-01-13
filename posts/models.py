from django.db import models

class Post(models.Model):
    profile_image = models.ImageField(upload_to='images/images')
    profile_bio = models.CharField(max_length=50)

    def __str__(self):
        return self.profile_bio
