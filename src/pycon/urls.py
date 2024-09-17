from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, {'lang': 'es'}, name="home"),
    path('es/', views.home, {'lang': 'es'}, name="home_es"),
    path('en/', views.home, {'lang': 'en'}, name="home_en"),
    path('conduct/', views.conduct, {'lang': 'es'}, name="conduct"),
    path('en/conduct/', views.conduct, {'lang': 'en'}, name="conduct_en"),
    path('scheduled/', views.scheduled, {'lang': 'es'}, name="scheduled"),
    path('en/scheduled/', views.scheduled, {'lang': 'en'}, name="scheduled_en"),
    path('en/tickets/', views.tickets, {'lang': 'en'}, name="tickets_en"),
    path('tickets/', views.tickets, {'lang': 'es'}, name="tickets"),
    path('team/', views.team, {'lang': 'es'}, name="team"),
    path('en/team/', views.team, {'lang': 'en'}, name="team_en"),
    path('pyladies/', views.pyladies, {'lang': 'es'}, name="pyladies"),
    path('en/pyladies/', views.pyladies, {'lang': 'en'}, name="pyladies_en"),

]