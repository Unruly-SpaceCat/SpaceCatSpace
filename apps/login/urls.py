from django.conf.urls import url
from . import views
#login urls

urlpatterns = [
    url(r'^$', views.index),
    url(r'^adduser$', views.adduser),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout)
]