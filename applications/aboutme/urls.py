from django.urls import path
from . import views

app_name = 'aboutme_app'

urlpatterns = [
    path('acerca-de-mi/', views.AboutMeView.as_view(), name='about-me'),
]
