import logging

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.views.decorators.cache import never_cache
from django.views.generic import UpdateView
from rest_framework.response import Response

from ScanCraft.apps.core.forms import InputFileForm
from ScanCraft.apps.core.models import InputFile

logger = logging.getLogger(__name__)  # Logger instance


def index(request):
    # return HttpResponse("Hello, world. You're at the images index.")
    template = loader.get_template('base_generic.html')
    context = {
        'title': 'Index'
    }
    return HttpResponse(template.render(context, request))


def thumbnail(request):
    # return HttpResponse("Hello, world. You're at the images index.")
    template = loader.get_template('thumbnail.html')
    context = {
        'title': 'Thumbnail'
    }
    return HttpResponse(template.render(context, request))


def upload(request):
    # return HttpResponse("Hello, world. You're at the images index.")
    template = loader.get_template('upload.html')
    model = InputFile
    form = InputFileForm

    context = {
        'title': 'Upload',
        'form': form
    }
    return HttpResponse(template.render(context, request))
