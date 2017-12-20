from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
#from django.views.generic.base import TemplateView
from appPrincipale import views as appPrincipale_views
from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'appPrincipale/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'appPrincipale/login.html'}, name='logout'),
    #url(r'^home/$', TemplateView.as_view(template_name='appPrincipale/home.html'), name='home'),
    url(r'^signup/$', appPrincipale_views.signup, name='signup'),
    url(r'^home/$', views.home, name='home'),
    url(r'^lieuR/(?P<lieu_id>[0-9]+)/$', views.lieuR, name='lieuR'),
]