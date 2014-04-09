from django.shortcuts import render_to_response
from django.template import RequestContext
from randomgroup.models import *

def home(request):
    """
    Select and render a random student group.
    """
    group = Group.objects.random()
    return render_to_response('group.html',
                              locals(),
                              context_instance=RequestContext(request))

