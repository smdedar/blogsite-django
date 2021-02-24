from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_view, name='index'),
    path('postcreate', views.post_create, name='index'),
]
