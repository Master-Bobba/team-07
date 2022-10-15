from django.urls import path
from .views import AuthURL, get_token, spotify_callback, IsAuthenticated
from . import views

app_name = 'guitar'

urlpatterns = [
    path('get-auth-url', AuthURL.as_view()),
    path('redirect', spotify_callback),
    path('is-authenticated', IsAuthenticated.as_view()),
    path('', views.index, name="index"),
    path('brand', views.brand, name='brand'),
    path('brands', views.brands, name='brands'),
    path('category', views.category, name='category'),
    path('categories', views.categories, name='categories'),
    path('guitar', views.guitar, name='guitar'),
    path('song', views.song, name='song'),


    path('getToken/', views.get_token, name = "get_token")
]