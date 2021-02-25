from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *


"""
urlpatterns = [
    path('<int:pk>/', PostDetailView.as_view()),
    path('', PostList.as_view()),

    path('users/', UserList.as_view()),  
    path('users/<int:pk>/', UserDetailView.as_view()),
]
"""

#REPLACING URLS WITH ROUTERS
#not for me though

router=SimpleRouter()
router.register('users',UserViewSet,basename='users')
router.register('',PostViewSet,basename='posts')

urlpatterns=router.urls