from django.contrib import admin
from django.urls import path , include
import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('home/', include('home.urls')),

]
