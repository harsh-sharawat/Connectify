from django.shortcuts import render,redirect
from .form import Create_room
# from .models import Room
from django.contrib import messages

from django.contrib.auth.decorators import login_required

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
        




    
