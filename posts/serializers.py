#y transforms data into JSON
# Specify which fields to include or excludE

from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('id', 'author', 'title', 'body', 'created_at',)

#list all users and individual users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=('id', 'username',)