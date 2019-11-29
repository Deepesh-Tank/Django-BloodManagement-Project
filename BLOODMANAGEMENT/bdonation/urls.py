"""bdonation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from blood import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blood.urls')),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('need',views.need,name='need'),
    path('donate',views.donate,name='donate'),
    path('index1',views.index1,name='index1'),
    path('index2',views.index2,name='index2'),
    path('facts',views.facts,name='facts'),
    path('test',views.test,name='test'),
    path('test1',views.test1,name='test1'),
    path('requestlist',views.requestlist,name='requestlist'),
    path('donorlist',views.donorlist,name='donorlist'),
    path('dlist',views.dlist,name='dlist'),
    path('rlist',views.rlist,name='rlist'),
    path('sing',views.sing,name='sing'),
    path('check',views.check,name='check'),
    path('chart1',views.chart1,name='chart1'),
]
