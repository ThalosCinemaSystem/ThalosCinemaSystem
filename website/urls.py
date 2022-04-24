from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('account/', views.account, name="account"),
    path('events_and_promotions/', views.events_and_promotions, name="events_and_promotions"),
    path('marathons/', views.marathons, name="marathons"),
    path('repertoire/', views.repertoire, name="repertoire"),
    path('schools/', views.schools, name="schools"),
]
