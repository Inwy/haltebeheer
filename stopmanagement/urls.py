from django.conf.urls import patterns, url
from django.views.generic import RedirectView, TemplateView

urlpatterns = patterns('',
    # Onze Index
    url(r'^$', RedirectView.as_view(url='/kaart')),

    # Kaart views
    url(r'^kaart$', TemplateView.as_view(template_name='stopmanagement/index.html'), name="stop_map"),
)