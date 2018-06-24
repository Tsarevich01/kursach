from django.urls import path, include, re_path

from blog import views, admin

#from blog.views import archive

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^about', views.about, name='about'),


]