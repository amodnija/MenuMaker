from django.urls import path
from . import views
urlpatterns = [
    path('menu', views.MenuDispView, name='display menu'),    
    path('menu2', views.MenuSaveView, name='display menu')
]
