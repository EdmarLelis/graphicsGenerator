from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.selector, name="selector"),
    path('graphic/', views.graphic, name='graphic')
]