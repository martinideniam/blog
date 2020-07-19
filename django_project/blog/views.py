from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'vlad',
        'title': 'well, fuck you',
        'content': 'some content in here',
        'date_posted': 'August 27, 2020'

    },
    {
        'author': 'zakhar',
        'title': 'well, e you',
        'content': 'some ff in here',
        'date_posted': 'August 27, 2020'

    },

    {
        'author': 'lera',
        'title': 'well, a you',
        'content': 'some asdasd in here',
        'date_posted': 'August 27, 2020'

    }

]


def home(request):
    context = {'posts': posts}
    return render(request,  'blog/home.html', context)


def about(request):
    context = {'posts': posts, 'title': 'about page'}
    return render(request,  'blog/about.html', context)

    # 07:35
