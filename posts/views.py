from rest_framework import generics,viewsets
from django.contrib.auth import get_user_model
from .serializers import PostSerializer, UserSerializer

from .models import *
from .serializers import *
from .permissions import *


# Create your views here.

"""
#to list,create the api data
class PostList(generics.ListCreateAPIView):
    #only authenticated, registered users have access
    #permission_classes=(permissions.IsAuthenticated,)
    queryset=Post.objects.aggregate()
    serializer_class=PostSerializer

#update,delete
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes=(permissions.IsAuthenticated,)
    permission_classes=(IsAuthor,)
    queryset=Post.objects.all()
    serializer_class=PostSerializer

    
#list all users and individual users

class UserList(generics.ListCreateAPIView):
    #only authenticated, registered users have access
    #permission_classes=(permissions.IsAuthenticated,)
    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes=(permissions.IsAuthenticated,)
    #permission_classes=(IsAuthor,)
    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer

"""

#REPLACING VIEWS WITH VIEWSETS
#not for me though
#FOR POSTS
class PostViewSet(viewsets.ModelViewSet): 
    permission_classes = (IsAuthor,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#FOR USERS
class UserViewSet(viewsets.ModelViewSet): 
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer