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
from pages import views
from test_submit.views import submit_data

urlpatterns = [
    path('admin/', 						admin.site.urls),
   	path('',							views.login_request,			name='home'), 
    path('home/',          views.login_request,   name='home'),   
   	#ath('home/',						home_view,			name='home'),
    #path('login/',          login_request,   name='login'),
   	path('loggedin/',					views.loggedin_view,		name='loggedin'),    
   	path('questions/<int:index>/',					views.questions_view,		name='questions'),
    path('questions/',          views.questions_view,   name='questions'),
    path('logout/',          views.logout_request,   name='logout'),
   	path('loggedout/',					views.loggedout_view,		name='loggedout'),
    path('register/',          views.register_view,   name='register'),
    path('submit_data/', submit_data)
]
