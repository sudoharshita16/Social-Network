from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class UserProfile(models.Model):  
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name="profile")  
    followers = models.ManyToManyField(User, related_name="following",null = True)
    bio = models.CharField(max_length = 200, blank = True)

    def __str__(self):
        return f"{self.user}"


class Post(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE, related_name = "posts")
    data = models.TextField(null = True)
    time = models.DateTimeField()
    likers = models.ManyToManyField(User, related_name = "liked_posts")
    
    def __str__(self):
        return f"{self.data} by {self.user}"





