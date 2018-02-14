from django.contrib import admin
from django.urls import path , include
import user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('home/', include('home.urls')),

]
