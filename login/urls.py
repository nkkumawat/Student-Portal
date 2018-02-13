from django.contrib import admin
from django.urls import path
from login import views
from django.conf.urls import url


urlpatterns = [
    path('auth', views.auth , name="auth"),
    path('', views.login , name="login"),
    path('signup', views.sign_up_page , name="signup"),
    path('create-user', views.sign_up , name="create-user"),
]
