from django.conf.urls import url
from . import views
from database import views as db_views

app_name = 'search'
urlpatterns = [
  
  url(r'^genes/$', views.genes),
  url(r'^organisms/$', views.organisms),
  url(r'^ligands/$', views.ligands),
  url(r'^$', db_views.index, name="index"),
  url(r'^record/(?P<riboswitch_name>([A-Za-z0-9|\W])+)/$', views.record, name="record"),
]
