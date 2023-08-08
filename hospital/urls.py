"""hospital URL Configuration

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
from django.urls import path
from app1 import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.home),
    path('login1/',views.login1),
    path('new_user_dr/',views.new_user1),
    path('new_user_nr/',views.new_user2),
    path('new_user_mn/',views.new_user3),
    path('new_user_off/',views.new_user4),
    path('new_user_sec/',views.new_user4),

    path('new_user/',views.new_user_page),
    path('inser_new_user/',views.inser_new_user_dtls),
    

]
