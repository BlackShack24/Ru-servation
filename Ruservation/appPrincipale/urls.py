from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'appPrincipale/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'appPrincipale/login.html'}, name='logout'),
    url(r'^$', TemplateView.as_view(template_name='appPrincipale/home.html'), name='home'),
    #url(r'^home/$', views.home, name='home'),
    #url(r'^admin/', admin.site.urls),
]