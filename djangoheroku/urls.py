"""djangoheroku URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,re_path
from djangoheroku import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form',views.form),
    path('',views.index,name='index'),
    path('testpage',views.test,name = 'test'),
    path('index',views.testInclude,name = 'test_include'),
    path('static-media',views.static_media,name = 'static_media'),
    path('static-css',views.static_css),
    path('static-js',views.static_js)
]
