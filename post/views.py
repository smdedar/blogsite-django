from django.shortcuts import redirect, render, HttpResponse
from . import models

# Create your views here.

def index(request):
    posts = models.post.objects.all()
    #return HttpResponse(posts)
    return render(request, 'index.html', {'posts':posts})


def details(request,pk):
    post = models.post.objects.get(id=pk)
    #return HttpResponse(post)
    return render(request, 'post.html', {'post':post})