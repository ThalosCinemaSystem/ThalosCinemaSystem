from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('maratony', views.maratons, name="maratons"),
    path('szkoly', views.schools, name="schools"),
]
