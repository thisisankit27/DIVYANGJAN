from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('filterScheme', views.filterScheme, name='filterScheme'),
]
