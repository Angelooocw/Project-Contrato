from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from .models import Content


class ContentDetailView(DetailView):
    model = Content
    template_name = 'content/detail_content.html'

    def get_context_data(self, **kwargs):
        context = super(ContentDetailView, self).get_context_data(**kwargs)
        context['navbar'] = Content.objects.get_content('Información')
        return context
