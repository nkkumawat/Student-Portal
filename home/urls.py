from django.contrib import admin
from django.urls import path
from home import views
from django.conf.urls import url


urlpatterns = [
    path('', views.home , name="home"),

]
