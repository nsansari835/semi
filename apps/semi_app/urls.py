from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^semi_app$', views.index),
    url(r'^semi_app/new$', views.new),
    url(r'^semi_app/(?P<id>\d+)/edit$', views.edit),
    url(r'^semi_app/(?P<id>\d+)$', views.show),
    url(r'^semi_app/create$', views.create),
    url(r'^semi_app/(?P<id>\d+)/destroy', views.destroy),
    url(r'^semi_app/(?P<id>\d+)/update', views.update),

]