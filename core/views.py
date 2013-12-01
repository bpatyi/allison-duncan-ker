from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.response import TemplateResponse
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.views.defaults import page_not_found
from django.shortcuts import render_to_response, get_object_or_404, redirect

from django.views.generic import View


class Index(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):

        context = {}

        return TemplateResponse(request, self.template_name, context)

