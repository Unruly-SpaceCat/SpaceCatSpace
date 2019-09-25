from django.conf.urls import url
from . import views
#dashboard urls

urlpatterns = [
    url(r'^(?P<username>\w+)$', views.index),
    url(r'^(?P<username>\w+)/edit$', views.editprofile),
    url(r'^(?P<username>\w+)/updateprofile$', views.updateprofile),
    url(r'^(?P<username>\w+)/friends$', views.allfriends),
    url(r'^(?P<username>\w+)/addfriend$', views.addfriend),
    url(r'^(?P<username>\w+)/removefriend$', views.removefriend),
    url(r'^(?P<username>\w+)/admin$', views.admin),
    url(r'^(?P<username>\w+)/admin/make$', views.adminmake),
    url(r'^(?P<username>\w+)/admin/ban$', views.adminban),
    url(r'^(?P<username>\w+)/admin/remove$', views.adminremove),
    url(r'^(?P<username>\w+)/private$', views.private),
    url(r'^(?P<username>\w+)/postconvo$', views.postconvo),
    url(r'^(?P<username>\w+)/(?P<id>\d+)/postreply$', views.postreply)
]