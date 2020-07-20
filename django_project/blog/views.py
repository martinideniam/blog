from django.shortcuts import render
from django.http import HttpResponse
from .models import post

# Create your views here.


def home(request):
    posts = post.objects.all()
    context = {'posts': posts}
    return render(request,  'blog/home.html', context)


def about(request):
    context = {'posts': posts, 'title': 'about page'}
    return render(request,  'blog/about.html', context)

    # 07:35
