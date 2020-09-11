from django.urls import path
from . import views

app_name = 'content_app'

urlpatterns = [
    path('content/<pk>', views.ContentDetailView.as_view(), name='content-detail')
]
