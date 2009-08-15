from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import list_detail
from models import Paste

def paste_list(request, **kwargs):
    "render the paste list page"
    if request.user.is_authenticated():
        pastes = Paste.objects.exclude(active=False)
    else:
        pastes = Paste.objects.exclude(active=False).exclude(public=False)
    import ipdb
    ipdb.set_trace()
    context = {
        "pastes": pastes,
    }
    return render_to_response('paste_organizer/paste_list.html', context,
        context_instance=RequestContext(request))
