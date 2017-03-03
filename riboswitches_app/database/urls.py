from django.conf.urls import url
from . import views

app_name = 'database'

urlpatterns = [
	url(r'^$', views.index, name="index"),
    url(r'^ligand_browser/$', views.ligand_browser, name='ligand_browser'),
    url(r'^ligand_browser/(?P<ligand_name>[A-Za-z]+)/$', views.ligand_detail, name="ligand_detail"),
    url(r'^organism_browser/$', views.organism_browser, name='organism_browser'),
    url(r'^organism_browser/(?P<organism_name>([-\w\s.()])+)/$', views.organism_detail, name="organism_detail"), ##TODO REGEX!!!
    url(r'^searcher/', views.searcher, name='searcher'),
]