from django.shortcuts import render
from django.views.generic import TemplateView
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
        return context
