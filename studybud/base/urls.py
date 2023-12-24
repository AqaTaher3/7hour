from django.urls import path
from . import views

urlpatterns = [
    path('/', views.home, name="home"),
    path('romm/<str:pk>', views.room, name="room"),
]
