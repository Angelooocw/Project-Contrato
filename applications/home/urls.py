from django.urls import path
from . import views

app_name = 'home_app'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('contacto/', views.ContactFormView.as_view(), name='contact'),
    path('search/', views.SearchResultView.as_view(), name='search')
]
