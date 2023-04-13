from django.urls import path
from . import views

urlpatterns = [
    path('contactSend', views.contactSend, name='contactSend'),
]
