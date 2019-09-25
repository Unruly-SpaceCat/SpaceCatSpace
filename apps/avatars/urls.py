from django.conf.urls import url
from . import views
#avatars urls

urlpatterns = [
    url(r'^$', views.index), 
    url(r'^editavatar$', views.update)
]