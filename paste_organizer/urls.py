from django.conf.urls.defaults import *
from models import Paste

paste_list_dict = {
  'queryset': Paste.objects.all(),
}

urlpatterns = patterns('',
    (r'$','django.views.generic.list_detail.object_list',
        paste_list_dict),
)
