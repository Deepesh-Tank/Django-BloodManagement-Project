from django.conf.urls import url
from django.urls import path
from blood import views


urlpatterns = [
    path('',views.index,name='index'),
    path('abcd',views.temp,name='temp'),
    path('don',views.don,name='don'),
    path('req',views.req,name='req'),
    path('index',views.index,name='index'),
]
