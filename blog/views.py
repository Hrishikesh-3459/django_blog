from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': "Alice",
        'title': 'Title_1',
        'content': 'content1',
        'date_posted': 'date1'
    },
    {
        'author': "Bob",
        'title': 'Title_2',
        'content': 'content2',
        'date_posted': 'date2'
    }
]
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html")

