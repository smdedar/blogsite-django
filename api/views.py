from re import A
from django.http import response
from django.shortcuts import render, HttpResponse
from post.models import post
from . import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

def index(request):
    posts = post.objects.all()
    return HttpResponse(posts)

@api_view(['GET'])
def post_view(request):
    posts = post.objects.all()
    serializer = serializers.PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_create(request):
    serializer = serializers.PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response('Post Create Successfully')