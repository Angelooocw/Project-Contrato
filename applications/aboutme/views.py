from django.shortcuts import render
from django.views.generic import TemplateView

from applications.content.models import Content
from .models import Perfil, Fallo, Publicacion


class AboutMeView(TemplateView):
    template_name = 'about_me/aboutme.html'

    def get_context_data(self, **kwargs):
        context = super(AboutMeView, self).get_context_data(**kwargs)
        context['navbar'] = Content.objects.get_content('Información')
        context['data'] = Perfil.objects.filter().order_by('-created').first()
        context['responsabilidades'] = Content.objects.get_content('Responsabilidades')
        context['encargo'] = Content.objects.get_content('Encargo del Proyecto')
        context['inspeccion'] = Content.objects.get_content('Inspección Técnica')
        context['info'] = Content.objects.get_content('info_sidebar')
        context['fallos'] = Fallo.objects.all().order_by('-created')
        context['publicaciones'] = Publicacion.objects.all().order_by('-created')
        return context
