from django.shortcuts import render
from django.views.generic import TemplateView
from applications.content.models import Content
from .models import Home

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['home'] = Home.objects.filter().order_by('-created').first()
        context['importants'] = Content.objects.get_important_content()
        return context
