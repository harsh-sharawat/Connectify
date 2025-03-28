from django.db import models
from django.contrib.auth.models import User

from django.utils.timezone import now

# Create your models here.

class Room(models.Model):
    room_name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'created_rooms')
    created_at = models.DateTimeField(auto_now_add = True)

    description = models.CharField(max_length=500)
    tags = models.CharField(max_length=500)

    members = models.ManyToManyField(User, related_name='joined_rooms', blank=True)

    is_private = models.BooleanField(default=False)

    


class Chat(models.Model):

    room = models.OneToOneField(Room,on_delete=models.CASCADE, related_name= 'chat')
    messages = models.JSONField(default = list)
    
    def add_message(self , sender, content):
        message ={
            'content':content,
            'sender':sender,
            'time':now().isoformat()
        }

        self.messages.append(message)
        self.save(update_fields=['messages'])



