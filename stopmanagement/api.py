from tastypie.resources import ModelResource
from stopmanagement.models import Town

class TownResource(ModelResource):
  class Meta:
    queryset = Town.objects.all()
    resource_name = 'town'

#from myapp.models import Entry
#
#
#class EntryResource(ModelResource):
#    class Meta:
#        queryset = Entry.objects.all()
#        resource_name = 'entry'