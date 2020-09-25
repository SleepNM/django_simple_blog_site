from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
]
