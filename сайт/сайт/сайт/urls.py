"""сайт URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from templates import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url("ladozh", views.ladozhRender, name='ladozh'),
    url("mosk", views.moskRender, name='mosk'),
    url("vhod", views.vhodRender, name='vhod'),
    url("polz", views.polzRender, name='polz'),
    url("regist", views.Regist, name='regist'),
    path('admin/', admin.site.urls),
    path('<int:id>', views.trainViewRender),
    path('<int:id>m', views.train1ViewRender),

]
