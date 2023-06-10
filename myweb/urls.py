"""
URL configuration for myweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myweb.views import handle_404
from django.shortcuts import render,redirect
from contact.views import contact_view


handler404 = 'myweb.views.handle_404'



from . import views

urlpatterns = [
    path('', views.homepg),
    path('about-us/', views.aboutus),
    path('contact-us/', views.contactus),
    path('packages/', views.packages),
    path('admin/', admin.site.urls),
    path('contact/', contact_view, name='contact'),

    
]






