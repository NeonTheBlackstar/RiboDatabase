from django.conf.urls import url
from . import views
from database import views as db_views

app_name = 'search'
urlpatterns = [
  
  url(r'^riboswitches/$', views.riboswitches),
  url(r'^ligands/$', views.ligands),
  url(r'^$', db_views.index, name="index"),
]
