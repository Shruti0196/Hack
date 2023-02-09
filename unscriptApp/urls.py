from django.urls import path
from . import views
from .views import *

urlpatterns=[
 path('signup/',signup.as_view(),name='signup'),
 path('sample/',views.sample,name='sample'),
 path('login/',views.login,name='login'),
]