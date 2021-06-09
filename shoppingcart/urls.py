from django.conf.urls import url
from . import views
from django.urls import path, re_path

app_name = 'shoppingcart'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
]
