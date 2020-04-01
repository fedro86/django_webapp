from django.shortcuts import render
from .models import Post


# Sono finiti tutti in models
# posts = [{
#
#     'author': 'Corey Taylor',
#     'title': 'Blog post 1',
#     'content': 'First post content',
#     'date_posted': 'August, 27 2020'
#
#     },
#     {
#     'author': 'Amelia Taylor',
#     'title': 'Blog post 2',
#     'content': 'Second post content',
#     'date_posted': 'August, 28 2020'
#
#     }
# ]


def home(request):
    context = {
        'posts': Post.objects.all() #al posto di 'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

