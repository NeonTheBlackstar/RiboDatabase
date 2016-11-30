from django.conf.urls import url
from . import views

app_name = 'database'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^searcher/$', views.searcher, name="searcher")
]