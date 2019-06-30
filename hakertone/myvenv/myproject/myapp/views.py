from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

#def page_not_found(request, exception):
#    response = render_to_response('page_404.html', {}, context_instance=RequestContext(request))
#    response.status_code = 404
#    return response

def page_404(request, exception):
    return render(request, 'page_404.html', status=404)
    