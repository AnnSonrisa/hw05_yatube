from django.urls import path

from . import views

app_name = 'about'

urlpatterns = [
    path('author/', views.About.as_view(),
         name='about_author'),
    path('tech/', views.Tech.as_view(),
         name='tech'),
]
