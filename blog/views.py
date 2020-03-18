from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def python(request):
    posts = Post.objects.filter(related_language="python")
    return render(request, 'blog/python.html', {'posts': posts})

def sqlnosql(request):
    posts = Post.objects.filter(related_language="sqlnosql")
    return render(request, 'blog/sqlnosql.html', {'posts': posts})

def webdevelpment(request):
    posts = Post.objects.filter(related_language="htmlcssjavascript")
    return render(request, 'blog/web.html', {'posts': posts})

def scripting(request):
    posts = Post.objects.filter(related_language="scripting")
    return render(request, 'blog/scripting.html', {'posts': posts})