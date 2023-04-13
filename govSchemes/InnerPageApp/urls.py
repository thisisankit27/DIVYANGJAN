from django.urls import path
from . import views

urlpatterns = [
    path('physicalDisability', views.physicalDisability, name='physicalDisability'),
    path('intellectualDisability', views.intellectualDisability,
         name='intellectualDisability'),
    path('mentalDisability', views.mentalDisability, name='mentalDisability'),
    path('bloodDisorder', views.bloodDisorder, name='bloodDisorder'),
]
