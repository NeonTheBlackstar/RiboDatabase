from django.conf.urls import url
from . import views

app_name = 'database'

urlpatterns = [
	url(r'^index/$', views.index, name="index"),
    url(r'^browser/$', views.browser, name='browser'),
    url(r'^ligand/$', views.detail, name="detail"),
]