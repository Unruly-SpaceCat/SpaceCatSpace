from django.conf.urls import url
from . import views
#kithub urls

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<id>\d+)$', views.show),
    url(r'^addconvo$', views.addconvo),
    url(r'^(?P<id>\d+)/addcomment$', views.addcomment),
    url(r'^(?P<id1>\d+)/(?P<id2>\d+)/addreply$', views.addreply),
    url(r'APOD$', views.apod),
    url(r'^(?P<id>\d+)/delete$', views.deleteconvo),
    url(r'^(?P<id>\d+)/likeconvo$', views.likeconvo),
    url(r'^(?P<id1>\d+)/(?P<id2>\d+)/likecomment$', views.likecomment),
    url(r'^(?P<id1>\d+)/(?P<id2>\d+)/delete$', views.deletecomment),
]