from django.shortcuts import render
from django.views.generic import DetailView

from .models import Content


class ContentDetailView(DetailView):
    model = Content
    template_name = 'content/detail_content.html'
