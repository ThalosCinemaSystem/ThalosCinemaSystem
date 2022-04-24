from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('marathons', views.marathons, name="marathons"),
    path('schools', views.schools, name="schools"),
    path('account', views.account, name="account"),
    path('events_and_promotions', views.events_and_promotions, name="events_and_promotions"),
    path('repertoire', views.repertoire, name="repertoire"),
]
