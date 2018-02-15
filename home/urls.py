from django.contrib import admin
from django.urls import path
from home import views
from django.conf.urls import url


urlpatterns = [
    path('', views.home , name="home"),
    path('pay', views.payFees , name="pay"),
    path('profile', views.profile , name="profile"),
    path('result', views.result , name="result"),
    path('upload_pic', views.profile_pic_upload , name="Upload"),
    path('notifications', views.notifications , name="notifications"),

]
