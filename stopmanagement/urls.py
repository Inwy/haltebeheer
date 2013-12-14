from django.conf.urls import patterns, url, include
from django.views.generic import RedirectView, TemplateView
from stopmanagement.api import TownResource

town_resource = TownResource()

urlpatterns = patterns('',
    # Onze Index
    url(r'^$', RedirectView.as_view(url='/kaart')),

    # Kaart views
    url(r'^kaart$', TemplateView.as_view(template_name='stopmanagement/index.html'), name="stop_map"),

    (r'^api/', include(town_resource.urls)),
)