from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    """
    Select and render a random student group.
    """
    return render_to_response('group.html',
                              context_instance=RequestContext(request))
