from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'appPrincipale/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
<<<<<<< HEAD
    url(r'^home/$', views.home, name='home'),
=======
>>>>>>> de91449ee05afe6ce10b4029b627d3dd95d5e0d8
    #url(r'^admin/', admin.site.urls),
]