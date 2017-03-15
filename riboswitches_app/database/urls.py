from django.conf.urls import url
from . import views

app_name = 'database'

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^browser/ligand/$', views.ligand_browser, name='ligand_browser'),
    url(r'^browser/ligand/(?P<ligand_name>[A-Za-z]+)/$', views.ligand_detail, name='ligand_detail'),
    url(r'^browser/organism/$', views.organism_browser, name='organism_browser'),
    url(r'^browser/organism/(?P<organism_name>([-\w\s.()])+)/$', views.organism_detail, name='organism_detail'),

    url(r'^browser/class/$', views.class_family_detail, name="class_family_detail"),
    #url(r'^browser/class/(?P<class_name>([-\w\s.()])+)/$', views.class_family_detail, name='class_family_detail'),
    url(r'^searcher/', views.searcher, name='searcher'),
]