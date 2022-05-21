from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('book/<str:projection_pk>/', views.book_movie, name='book'),
    path('<str:pk>/', views.main_page),
    path('<str:pk>/<str:pk2>', views.main_page),
    path('<str:pk>/<str:pk2>/<str:pk3>', views.main_page),
    path('<str:pk>/<str:pk2>/<str:pk3>/<int:pk4>', views.main_page),
    path('logout', views.logoutUser, name="logout"),
    path('marathons', views.marathons, name="marathons"),
    path('schools', views.schools, name="schools"),
    path('account', views.account, name="account"),
    path('events_and_promotions', views.events_and_promotions, name="events_and_promotions"),
    path('repertoire', views.repertoire, name="repertoire"),
    path('change-password', views.change_password, name='change_password'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)