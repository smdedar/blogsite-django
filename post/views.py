from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.

def index(request):
    posts = models.post.objects.all()
    #return HttpResponse(posts)
    return render(request, 'post.html', {'posts':posts})
