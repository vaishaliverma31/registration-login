from django.urls import path
from django.urls.conf import include
from .views import *
 
 
urlpatterns = [

    path('register',regiteruserapi.as_view()),
    path('login',LoginApiView.as_view())
]
