from django.urls import path
from .views import AuthURL, spotify_callback, IsAuthenticated
from . import views

urlpatterns = [
    path('get-auth-url', AuthURL.as_view()),
    path('redirect', spotify_callback),
    path('is-authenticated', IsAuthenticated.as_view()),
    path('', views.index, name='index')
]