from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse
from applications.content.models import Content
from .models import Home
from .forms import ContactForm

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['home'] = Home.objects.filter().order_by('-created').first()
        context['importants'] = Content.objects.get_content('Importante')
        context['navbar'] = Content.objects.get_content('Información')
        context['responsabilidades'] = Content.objects.get_content('Responsabilidades')
        context['encargo'] = Content.objects.get_content('Encargo del Proyecto')
        context['inspeccion'] = Content.objects.get_content('Inspección Técnica')
        context['info'] = Content.objects.get_content('info_sidebar')
        context['capacitaciones'] = Content.objects.get_content('Capacitación')
        return context


class ContactFormView(FormView):
    template_name = 'home/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('')

    def get_context_data(self, **kwargs):
        context = super(ContactFormView, self).get_context_data(**kwargs)
        context['navbar'] = Content.objects.get_content('Información')
        context['responsabilidades'] = Content.objects.get_content('Responsabilidades')
        context['encargo'] = Content.objects.get_content('Encargo del Proyecto')
        context['inspeccion'] = Content.objects.get_content('Inspección Técnica')
        context['info'] = Content.objects.get_content('info_sidebar')
        return context


class SearchResultView(ListView):
    model = Content
    template_name = 'home/search_res.html'
    context_object_name = 'list_res'

    def get_context_data(self, **kwargs):
        context = super(SearchResultView, self).get_context_data(**kwargs)
        context['navbar'] = Content.objects.get_content('Información')
        context['responsabilidades'] = Content.objects.get_content('Responsabilidades')
        context['encargo'] = Content.objects.get_content('Encargo del Proyecto')
        context['inspeccion'] = Content.objects.get_content('Inspección Técnica')
        context['info'] = Content.objects.get_content('info_sidebar')
        return context

    def get_queryset(self):
        kword = self.request.GET.get('kword', '')
        query = Content.objects.filter(
            title__icontains=kword
        ) | Content.objects.filter(
            content__icontains=kword
        )
        queryset = query.order_by('-created')
        return queryset
