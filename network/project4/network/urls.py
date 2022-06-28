
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("profile/<int:pid>", views.profile, name="profile"),
    path("following_post", views.following_post, name="following_post"),
    path("edit", views.edit, name="edit"),
    path("follow", views.follow, name="follow"),
    path("unfollow", views.unfollow, name="unfollow"),
    path("profile/fval/<int:puser_id>", views.fval, name='fval'),
    path("like_unlike",views.like_unlike, name="like_unlike"),
    path("following_post/lval/<int:pid>",views.lval, name="lval"),
    path("lval/<int:pid>",views.lval,name="lval"),
    path("eval/<int:pid>", views.eval, name="eval"),
    path("prof",views.profile,name="prof"),
    path("edit_bio",views.edit_bio,name="edit_bio")
   
]
