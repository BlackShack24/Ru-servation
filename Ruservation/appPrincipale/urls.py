from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from appPrincipale import views as appPrincipale_views
from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'appPrincipale/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'appPrincipale/login.html'}, name='logout'),
    url(r'^signup/$', appPrincipale_views.signup, name='signup'),
    url(r'^home/$', views.home, name='home'),
    url(r'^lieuR/(?P<lieu_id>[0-9]+)/(?P<user_id>[0-9]+)/$', views.lieuR, name='lieuR'),
    url(r'^profil/(?P<user_id>[0-9]+)/$', views.profil, name='profil'),
    url(r'^addFav/(?P<lieu_id>[0-9]+)/(?P<user_id>[0-9]+)/$', views.addFav, name='addFav'),
    url(r'^favoris/(?P<user_id>[0-9]+)/$', views.favoris, name='favoris'),
    url(r'^parametres/(?P<user_id>[0-9]+)/$', views.parametres, name='parametres'),
    url(r'^getParam/(?P<user_id>[0-9]+)/$', views.get_Param, name='getParam'),
    url(r'^geoLoc/(?P<lieu_id>[0-9]+)/$', views.geoLoc, name='geoLoc'),
    url(r'^reservation/(?P<lieu_id>[0-9]+)/(?P<user_id>[0-9]+)/$', views.reservation, name='reservation'),
    url(r'^profil/(?P<lieu_id>[0-9]+)/(?P<user_id>[0-9]+)/(?P<platP_id>[0-9]+)/$', views.resDone, name='resDone'),
    url(r'^historique/(?P<user_id>[0-9]+)/$', views.historique, name='historique'),
]