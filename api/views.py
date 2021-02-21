from django.shortcuts import render, HttpResponse
from post.models import post
# Create your views here.

def index(request):
    posts = post.objects.all()
    return HttpResponse(posts)