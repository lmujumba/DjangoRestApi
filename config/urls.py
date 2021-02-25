"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#for dynamic schema generation
from rest_framework.schemas import get_schema_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view=get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version="v1",
        description="A sample API for learning DRF in django and python",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="hello@example.com"),
        license=openapi.License(name="BSD License"),

    ),
    public=True,
    #COMMAS IN PERMISSION CLASSES
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('posts.urls')),

    #matches documentation
    #to add log out option to  the api
    path('api-auth/',include('rest_framework.urls')),

    #add 3rd party auth urls
    path('api/v1/dj_rest_auth/',include('dj_rest_auth.urls')),

    #registration and stuff
    path('api/v1/dj_rest_auth/registration/',include('dj_rest_auth.registration.urls')),


    #for schema and documentation

    path('swagger/', schema_view.with_ui( 
    'swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('redoc/', schema_view.with_ui( 
    'redoc', cache_timeout=0), name='schema-redoc'),
    
]
