from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, {'lang': 'es'}, name="home"),
    path('es/', views.home, {'lang': 'es'}, name="home_es"),
    path('en/', views.home, {'lang': 'en'}, name="home_en"),
    path('scheduled/', views.scheduled, {'lang': 'es'}, name="scheduled"),
]