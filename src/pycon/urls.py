from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, {'lang': 'es'}, name="home"),
    path('es/', views.home, {'lang': 'es'}, name="home_es"),
    path('en/', views.home, {'lang': 'en'}, name="home_en"),
    path('conduct/', views.conduct, {'lang': 'es'}, name="conduct"),
    path('en/conduct/', views.conduct, {'lang': 'en'}, name="conduct_en"),
    path('es/conduct/', views.conduct, {'lang': 'es'}, name="conduct_es"),
    path('scheduled/', views.scheduled, {'lang': 'es'}, name="scheduled"),
    path('en/scheduled/', views.scheduled, {'lang': 'en'}, name="scheduled_en"),
    path('es/scheduled/', views.scheduled, {'lang': 'es'}, name="scheduled_es"),
]