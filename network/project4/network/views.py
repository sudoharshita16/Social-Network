from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.core.paginator import Paginator

from .models import User, UserProfile, Post


def index(request):
    entries = Post.objects.order_by('pk')
    entries = entries.reverse()
    if request.user.is_authenticated:
        userobj = User.objects.get(pk=request.user.id)
    else:
        userobj = User.objects.get(pk=1)
    paginator = Paginator(entries, 10)
    if request.GET.get("page") != None:
        try:
            entries = paginator.page(request.GET.get("page")).object_list
            page_obj = paginator.get_page(request.GET.get("page"))
            #print(page_obj)
        except:
            entries = paginator.page(1).object_list
            page_obj = paginator.get_page(1)
    else:
        entries = paginator.page(1).object_list
        page_obj = paginator.get_page(1)
    ids = entries.values_list('pk',flat = True)
    ids = list(ids)
    ids.sort()
    ids.reverse()
    #print(page_obj)
    return render(request, "network/index.html",{
        "entries":list(entries),
        "userobj":userobj,
        "ids":ids,
        "add_info":"all_posts",
        "page_obj":page_obj
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            # by Harshita
            new_profile = UserProfile(user=user,bio="Hey there! I am using network")
            print(new_profile)
            new_profile.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

#@login_required not working properly rn
def create(request):
    if request.method == "POST":
        data = request.POST["data"]
        print(request.user)
        print(request.user.id)
        username = User.objects.get(pk=request.user.id)
        p = Post(user=username, data=data,time=datetime.now())
        p.save()
        return HttpResponseRedirect(reverse("index"))

def profile(request,pid):
    userobj = User.objects.get(pk=pid)
    userprofile = userobj.profile
    posts = userobj.posts.all() 
    thisuserobj = User.objects.get(pk=request.user.id)
    thisuserprofile = thisuserobj.profile
    if userobj in thisuserprofile.followers.all():
        follows_you = "follows you!"
    else:
        follows_you = "doesn't follow you :("   
    followers = userprofile.followers.all()
    following = userobj.following.all()
    if thisuserobj in userprofile.followers.all():
        show_follow_button = 0
    else:
        show_follow_button = 1   
    following = userobj.following.all()
    person_profile = userobj.profile
    posts = posts.order_by('-pk')
    paginator = Paginator(posts, 10)
    if request.GET.get("page") != None:
        try:
            entries = paginator.page(request.GET.get("page")).object_list
            page_obj = paginator.get_page(request.GET.get("page"))
            print(page_obj)
        except:
            entries = paginator.page(1).object_list
            page_obj = paginator.get_page(1)
    else:
        entries = paginator.page(1).object_list
        page_obj = paginator.get_page(1)
    ids = entries.values_list('pk',flat = True)
    ids = list(ids)
    ids.sort()
    ids.reverse()
    print(page_obj)
    
    return render(request, 'network/profile.html',{
        "posts":entries,
         "nfollowing": following.count(),
        "nfollowers": followers.count(),
        "follows":follows_you,
        "person_profile": person_profile,
        "show_follow_button":show_follow_button,
        "puser":person_profile.user,
        "person_id":userobj.id,
        "page_obj":page_obj

        })
       

def following_post(request):
    following_posts = Post.objects.none()
    userobj = User.objects.get(pk=request.user.id)
    userprofile = userobj.profile
    followers = userprofile.followers.all()
    following = userobj.following.all()
    
    for person_obj in following:
        user_obj = person_obj.user
        following_posts = following_posts | user_obj.posts.all()
    
    entries = following_posts.order_by('-pk')
    paginator = Paginator(entries, 10)

    if request.GET.get("page") != None:
        try:
            entries = paginator.page(request.GET.get("page")).object_list
            page_obj = paginator.get_page(request.GET.get("page"))
            print(page_obj)
        except:
            entries = paginator.page(1).object_list
            page_obj = paginator.get_page(1)
    else:
        entries = paginator.page(1).object_list
        page_obj = paginator.get_page(1)

    ids = entries.values_list('pk',flat = True)
    ids = list(ids)
    ids.sort()
    ids.reverse()
    print(page_obj)

    return render(request, "network/index.html",{
        "entries":list(entries),
        "userobj":userobj,
        "ids":ids,
        "add_info":"following_posts",
        "page_obj":page_obj

    })

   
    
    
@csrf_exempt
def edit(request):
    #print("harshiiiii")
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        #print(data)
        pid = data.get("entry_id")
        #print(pid)
        text = data.get("text")
        #print(text)
        post  = Post.objects.get(pk=pid)
        post.data = text
        post.save()
        #print(post)
        return JsonResponse({"message": "Edit request sent successfully."}, status=201)


@csrf_exempt
def follow(request):
    #Follow  form must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        puser_id = data.get("puser_id")
        followers = data.get("followers")
        
        to_be_added_obj = User.objects.get(pk=puser_id)
        this_userobj = User.objects.get(pk=request.user.id)
       
        this_userobj.following.add(to_be_added_obj.profile)
        this_userobj.save()
       
        return JsonResponse({"message": "Follow request sent successfully."}, status=201)

@csrf_exempt
def unfollow(request):
    #unfollow form must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        puser_id = data.get("puser_id")
        followers = data.get("followers")

        to_be_removed_obj = User.objects.get(pk=puser_id)
        this_userobj = User.objects.get(pk=request.user.id)
       
        this_userobj.following.remove(to_be_removed_obj.profile)
        this_userobj.save()
       
        return JsonResponse({"message": "Unfollow request sent successfully."}, status=201)



def fval(request, puser_id):
    #print("reached fval functions")
    puser_profile = UserProfile.objects.get(id=puser_id)
    #print(puser_profile)
    followers = list(puser_profile.followers.all())
    #print(followers)
    followers_count = len(followers)
    #print(followers_count)
    return JsonResponse({"followers_count": followers_count}, status=201)


def lval(request,pid):
    print("reached lval function: ")
    postobj = Post.objects.get(id=pid)
    likes = len(postobj.likers.all())
    print(likes)
    return JsonResponse({"likes":likes},status=201)

def eval(request, pid):
    #print("reached eval function")
    postobj = Post.objects.get(id=pid)
    return JsonResponse({"text":postobj.data}, status=201)

@csrf_exempt
def like_unlike(request):
    #print("WOOO")
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    else:
        data = json.loads(request.body.decode("utf-8"))
        #print(data)
        entry_id = data.get("entry_id")
        #print(entry_id)
        val = data.get("val")
        #print(val)
        this_userobj = User.objects.get(pk=request.user.id)
        this_postobj = Post.objects.get(pk=entry_id)
        if val == "yes":
            this_userobj.liked_posts.add(this_postobj)
        elif val == "no":
             this_userobj.liked_posts.remove(this_postobj)
        this_userobj.save()     
    return JsonResponse({"likers": len(this_postobj.likers.all()),"val":val}, status=201)    

