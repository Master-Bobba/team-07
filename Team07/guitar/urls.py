from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brand', views.brand, name='brand'),
    path('brands', views.brands, name='brands'),
    path('category', views.category, name='category'),
    path('categories', views.categories, name='categories'),
    path('guitar', views.guitar, name='guitar'),
    path('song', views.song, name='song'),
]