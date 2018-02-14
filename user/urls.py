from django.contrib import admin
from django.urls import path
from user import views
from django.conf.urls import url


urlpatterns = [
    path('auth', views.auth , name="auth"),
    path('login', views.login , name="login"),
    path('logout', views.logout , name="logout"),
    path('signup', views.sign_up_page , name="signup"),
    path('create', views.sign_up , name="create"),
    path('change_password', views.change_password , name="change_password"),
]
