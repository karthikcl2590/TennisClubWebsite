from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from ladder.models import PlayerProfile,Match
from django.template import RequestContext, loader


def index(request):
    print 1
    template = loader.get_template('index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def about(request):
    print 2
    template = loader.get_template('about.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def news(request):
    print 3
    template = loader.get_template('news.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def roster(request):
    print 4
    template = loader.get_template('roster.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def faq(request):
    print 5
    template = loader.get_template('faq.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def media(request):
    print 6
    template = loader.get_template('media.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def contact(request):
    print 7
    template = loader.get_template('contact.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def homepage(request):
    print 8
    template = loader.get_template('index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))