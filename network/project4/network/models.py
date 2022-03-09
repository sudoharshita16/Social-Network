from distutils.command.upload import upload
from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

class User(AbstractUser):
    pass

class UserProfile(models.Model):  
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name="profile")  
    followers = models.ManyToManyField(User, related_name="following",blank=True,null = True)
    bio = models.CharField(max_length = 200, blank = True)
    profile_pic = models.ImageField(upload_to='userProfiels',blank=True,null=True)

    def save(self, *args, **kwargs):
        super().save()
        if(self.profile_pic):
            img = Image.open(self.profile_pic.path)
            width, height = img.size  # Get dimensions

            if width > 300 and height > 300:
                # keep ratio but shrink down
                img.thumbnail((width, height))

            # check which one is smaller
            if height < width:
                # make square by cutting off equal amounts left and right
                left = (width - height) / 2
                right = (width + height) / 2
                top = 0
                bottom = height
                img = img.crop((left, top, right, bottom))

            elif width < height:
                # make square by cutting off bottom
                left = 0
                right = width
                top = 0
                bottom = width
                img = img.crop((left, top, right, bottom))

            if width > 300 and height > 300:
                img.thumbnail((300, 300))

            img.save(self.profile_pic.path)

    def __str__(self):
        return f"{self.user}"


class Post(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE, related_name = "posts")
    data = models.TextField(null = True)
    time = models.DateTimeField(blank=True)
    likers = models.ManyToManyField(User, related_name = "liked_posts",blank=True)
    post_image = models.ImageField(upload_to="postImg",blank=True,null=True)
    
    def __str__(self):
        return f"{self.data} by {self.user}"





