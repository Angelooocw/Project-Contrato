from django.urls import path
from . import views

app_name = 'content_app'

urlpatterns = [
    path('<slug>', views.ContentView.as_view(), name='content-detail'),
    path('importantes/', views.ImportantListView.as_view(), name='list-important')
]
