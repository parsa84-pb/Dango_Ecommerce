from django.urls import path

from .views import room, chat

urlpatterns = [
    path('chat/', chat),
    path('chat/<str:room_name>/', room, name='room')
]
