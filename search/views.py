# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView

import requests

# Search Function
# Search and Results Display On the Same Page
class SearchView(TemplateView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):

        context = super(SearchView, self).get_context_data(**kwargs)
        if 'term' in self.request.GET.keys() and self.request.GET['term']:
            url = 'https://autocomplete.clearbit.com/v1/companies/suggest'
            result = requests.get(url, params={'query': self.request.GET['term']})

            context['response'] = result.json()
        return context

    def get(self, request, *args, **kwargs):

        return super(SearchView, self).get(request, *args, **kwargs)
