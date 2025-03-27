from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from room.models import Room


def index(request):
    return render(request, 'core/index.html')

@login_required
def dashboard(request):

    rooms = Room.objects.all()


    context = {'rooms':rooms}
    return render(request, 'core/dashboard.html',context)
