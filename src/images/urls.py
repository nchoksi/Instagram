from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^upload/$', views.image_upload, name='upload'),
   # url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.image_detail, name='detail'),
]
