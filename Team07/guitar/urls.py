from django.urls import path
from .views import AuthURL, get_token, spotify_callback, IsAuthenticated
from . import views

app_name = 'guitar'

urlpatterns = [
    path('get-auth-url', AuthURL.as_view()),
    path('redirect', spotify_callback),
    path('is-authenticated', IsAuthenticated.as_view()),
    path('', views.index, name="index"),
    path("<str:category_id>", views.category, name="category"),
    path('brand/<str:brand_id>', views.brand, name='brand'),
    path("brands/", views.brands, name="brandZZ"),
    #path('category', views.category, name='category'),
    path('categories/', views.categories, name="categorieZZ"),
    path('guitar/<str:guitar_id>', views.guitar, name='guitar'),
    path('song', views.song, name='song'),


    path('getToken/', views.get_token, name = "get_token")
]