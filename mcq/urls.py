"""mcq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from pages.views import home_view, loggedin_view, questions_view, loggedout_view

urlpatterns = [
    path('admin/', 						admin.site.urls),
   	path('',							home_view,			name='home'),    
   	path('home/',						home_view,			name='home'),
   	path('loggedin/',					loggedin_view,		name='loggedin'),    
   	path('questions/',					questions_view,		name='questions'),
   	path('loggedout/',					loggedout_view,		name='loggedout')
]
