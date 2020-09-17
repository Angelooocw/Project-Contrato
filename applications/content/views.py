from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, ListView

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


class ImportantListView(ListView):
    model = Content
    template_name = 'content/important_list.html'
    context_object_name = 'important_list'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(ImportantListView, self).get_context_data(**kwargs)
        context['navbar'] = Content.objects.get_content('Información')
        context['responsabilidades'] = Content.objects.get_content('Responsabilidades')
        context['encargo'] = Content.objects.get_content('Encargo del Proyecto')
        context['inspeccion'] = Content.objects.get_content('Inspección Técnica')
        return context

    def get_queryset(self):
        response = Content.objects.get_content('Importante')
        return response
