# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .services import get_droplets

class GetDroplets(TemplateView):
    template_name = 'droplets.html'
    def get_context_data(self):
        context = {
            'droplets' : get_droplets(),
        }
        return context
