from django.urls import path
from . import views
urlpatterns = [
    path('', views.MenuDispView, name='current menu'),    
    path('edit', views.ImgChgView, name='change images')
]
