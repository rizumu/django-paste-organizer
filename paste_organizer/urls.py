from django.conf.urls.defaults import *
from views import paste_list

urlpatterns = patterns('',
    url(r"$", paste_list, name="paste_list"),
)
