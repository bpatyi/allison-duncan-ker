from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.response import TemplateResponse
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.views.defaults import page_not_found
from django.shortcuts import render_to_response, get_object_or_404, redirect

from django.views.generic import View

from section.models import Section
from collection.models import Collection, CollectionImage


class Index(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        try:
            sections = Section.objects.all()
        except Section.DoesNotExist:
            pass

        everything = {}

        for section in sections:
            collections = section.collection_set.all()

            everything[section.pk] = {
                'section': section,
                'collections': {},
            }

            for collection in collections:
                images = collection.collectionimage_set.all()
                if collection.pk not in everything[section.pk]['collections']:
                    everything[section.pk]['collections'][collection.pk] = { 'collection': collection, 'images': images } 

        context = {
            'sections': everything,
        }

        return TemplateResponse(request, self.template_name, context)


