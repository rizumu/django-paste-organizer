from django.conf.urls.defaults import *
from models import Writeboard

writeboard_list_dict = {
  'queryset': Writeboard.objects.all(),
}

urlpatterns = patterns('',
    (r'$','django.views.generic.list_detail.object_list',
        writeboard_list_dict),
)
