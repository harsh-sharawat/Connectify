from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from room.models import Room,Chat
from django.contrib import messages


@login_required
def feed(request, room_id):
    # authentication checks
    try:
        room = Room.objects.get(id = room_id)
    except Room.DoesNotExist:
        messages.error(request, "This room does not exists any more")
        return redirect('dashboard')
    
    if  not request.user.joined_rooms.filter(id = room_id).exists() :
        messages.error(request ,'Join the room first')
        return redirect('dashboard')
    
    try:
        chat = room.chat
       
    except Chat.DoesNotExist:
        chat = Chat.objects.create(room = room)
   

    context = {
        'room_name' : room.room_name,
        'room_id' : str(room_id),
        'history' : chat.messages,
        'user' : request.user.username
        
               }

    return render(request, 'feed/dash.html', context)



# Create your views here.
