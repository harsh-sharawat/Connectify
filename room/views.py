from django.shortcuts import render,redirect
from .form import Create_room
# from .models import Room
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .models import Room, Chat

# Create your views here.
@login_required
def create_room(request):


    if request.method == "POST":
        form  = Create_room(request.POST)

        if(form.is_valid()):
            room = form.save(commit= False)

            room.created_by = request.user
            room.save()
            room.members.add(request.user)
           
            if int(request.POST['typeofform']) == 2:
                room.is_private = True
            
           
            messages.success(request, "room created successfully!")
            return redirect('dashboard')
        else:
            messages.error(request, "room creation failed! Try again!")
            return redirect('create_room')
    else:
        form = Create_room()
    return render(request, 'room/create_room.html', {'form':form})
        
@login_required
def join_room(request,room_id):
    try:
        room = Room.objects.get(id = room_id)

    except Room.DoesNotExist:
        messages.error(request, 'this room does not exists')
        return redirect('dashboard')

    room.members.add(request.user)
    room.save()

    messages.success(request, "room joined successfully!")
    return redirect('dashboard')


@login_required
def leave_room(request, room_id):
    try:
        room = Room.objects.get(id = room_id)

    except Room.DoesNotExist:
        messages.error(request, 'this room does not exists')
        return redirect('dashboard')

    room.members.remove(request.user)
    room.save()

    messages.success(request, "room left successfully!")
    return redirect('dashboard')


@login_required
def my_rooms(request):

    rooms = request.user.joined_rooms.all()
    # print(type(rooms))




    context = {
        'rooms' : rooms
    }
    return render(request, 'room/myrooms.html',context)





    
