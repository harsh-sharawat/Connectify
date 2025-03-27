from django.urls import path,include
from . import views

urlpatterns = [
    path('create',views.create_room,name= 'create_room'),

    path('join_room/<int:room_id>',views.join_room, name = 'join_room'),
    path('leave_room/<int:room_id>',views.leave_room, name = 'leave_room'),
]
