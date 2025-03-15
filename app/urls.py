from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_view, name='inicio'),  # Página de inicio
    path('login/', views.login_view, name='login'),  # Página de login
    path('home/', views.home_view, name='home'),  # Página con el iframe y avatar
    path('logout/', views.logout_view, name='logout'),
    path('firebase-auth/', views.firebase_auth, name='firebase_auth'),
]
