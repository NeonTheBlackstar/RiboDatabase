from django.conf.urls import url
from . import views
from database import views as db_views

app_name = 'search'
urlpatterns = [
  
  url(r'^riboswitches/$', views.riboswitches),
  url(r'^ligands/$', views.ligands),
  url(r'^$', db_views.index, name="index"),
  url(r'^record/(?P<riboswitch_name>([A-Za-z0-9])+)/$', views.record, name="record"),
]
