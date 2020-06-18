from django.shortcuts import render
from django.utils import timezone
from .models import Post, Project
from django.views.decorators.clickjacking import xframe_options_exempt

def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    projects = Project.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/home.html', {'post0': posts[0], 'post1': posts[1], 'post2': posts[2],
                                              'project0': projects[0], 'project1': projects[1],
                                              'project2': projects[2], 'posts': posts})
def projects(request):
    projects = Project.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/projects.html', {'project0': projects[0], 'project1': projects[1],
                                                  'project2': projects[2], 'project3': projects[3], 'project4': projects[4],
                                                  'project5': projects[5]})
def about(request):
    return render(request, 'blog/about.html', {})

@xframe_options_exempt
def DE(request):
    return render(request, 'blog/DE.html', {})

@xframe_options_exempt
def tutorials(request):
    return render(request, 'blog/tutorials.html', {})