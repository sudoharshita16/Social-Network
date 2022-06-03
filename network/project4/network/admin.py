from django.contrib import admin
from .models import User, Post, UserProfile, Comments

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Comments)
