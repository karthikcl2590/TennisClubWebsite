from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from polls.models import PracticeInfo, PracticeInfoForm
from django.template import RequestContext
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.forms import ModelForm

# Create your views here
def index(request):
    form = PracticeInfoForm()
    return render_to_response('PracticeInfoForm.html',{'form': form})
    #    f request.method == 'POST':
    #    post = request.POST
    #    name = post['name']
    #    email = post['email']
    #    f = PracticeInfoForm(request.Post)
    #    new_info = f.save()
    #return render_to_response('PracticeInfoForm.html',
    #                               context_instance=RequestContext(request))
