"""django_test URL Configuration

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
网址入口，关联到对应的views.py中的一个函数（或者generic类），访问网址就对应一个函数。
"""
from django.contrib import admin
from django.urls import path
from test_demo1 import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('index/',views.index),
]
