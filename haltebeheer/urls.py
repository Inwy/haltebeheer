from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'haltebeheer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('stopmanagement.urls')),

    url(r'^inloggen/$', 'django.contrib.auth.views.login', {'template_name': 'users/login.html'}, name="app_login"),
    url(r'^uitloggen/$', 'django.contrib.auth.views.logout_then_login', name="app_logout"),
    url(r'^geweigerd/$', TemplateView.as_view(template_name="stopmanagement/nopermission.html"), name="app_nopermission"),
    url(r'^admin/', include(admin.site.urls)),
)
