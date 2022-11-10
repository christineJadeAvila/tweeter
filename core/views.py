from django.shortcuts import render
from django.http import HttpResponse

# example only

posts = [
    {'id':1, 'name': 'Jade', 'username': 'chjadeavila', 'post': 'Yo wazzup tweeter!'},
    {'id':2,'name': 'Erecka', 'username': 'ereckaAvila', 'post': 'married'},
]



# Create your views here.


def home(request):
    context = {
        'post': posts
    }
    return render(request, 'core/home.html', context)

def user_post(request, pk):

    post = None

    for indx in posts:
        if indx['id'] == int(pk):
            post = indx
    context = {
        'post': post
    }

    return render(request, 'core/user_post.html', context)

def messages(request):
    return render(request, 'core/messages.html')

def profile(request):
    return render(request, 'core/profile.html')

def user_settings(request):
    return render(request, 'core/settings.html')

def notifications(request):
    return render(request, 'core/notifications.html')

def bookmarks(request):
    return render(request, 'core/bookmarks.html')