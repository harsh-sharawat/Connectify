from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from room.models import Room


def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'core/index.html')

@login_required
def dashboard(request):

    rooms = Room.objects.all().order_by('-votecount')


    context = {'rooms':rooms}
    return render(request, 'core/dashboard.html',context)
