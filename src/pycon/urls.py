from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, {'lang': 'es'}, name="home"),
    path('es/', views.home, {'lang': 'es'}, name="home_es"),
    path('en/', views.home, {'lang': 'en'}, name="home_en"),
    path('conducta/', views.conduct, {'lang': 'es'}, name="conduct"),
    path('en/conducta/', views.conduct, {'lang': 'en'}, name="conduct_en"),
    path('es/conducta/', views.conduct, {'lang': 'es'}, name="conduct_es"),
    path('scheduled/', views.scheduled, {'lang': 'es'}, name="scheduled"),
]