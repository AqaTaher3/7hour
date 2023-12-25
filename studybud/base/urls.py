from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('', views.home, name='home'),
    path('room/<int:pk>/', views.room, name='room'),
    path('create/', views.create_room, name='create'),
    path('update/<str:pk>/', views.update_room, name='update-room'),
    path('delete/<str:pk>/', views.delete_room, name='delete-room'),
]
