from django.urls import path
from . import views

app_name = 'content_app'

urlpatterns = [
    path('content/<slug>', views.ContentView.as_view(), name='content-detail'),
]
