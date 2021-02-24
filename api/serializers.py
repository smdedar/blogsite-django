from django.db.models import fields
from rest_framework import serializers
from post.models import post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = '__all__'