from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from .models import Content


class ContentView(DetailView):
    model = Content
    template_name = 'content/detail_content.html'

    def get_context_data(self, **kwargs):
        context = super(ContentView, self).get_context_data(**kwargs)
        context['navbar'] = Content.objects.get_content('Información')
        context['responsabilidades'] = Content.objects.get_content('Responsabilidades')
        context['encargo'] = Content.objects.get_content('Encargo del Proyecto')
        context['inspeccion'] = Content.objects.get_content('Inspección Técnica')
        #context['contenido'] = Content.objects.get_detailed_data(self.kwargs['title'])
        return context
