from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from .form import Register

# Create your views here.


def login_page(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password= password)
        if user is not None:
            login(request, user)
           
           
            return redirect('dashboard')

            
        
        else:
            messages.error(request, 'wrong credentials')
            
            return redirect('login')



    return render(request, 'Authentication/login.html')

def logout_user(request):
    logout(request)
    return redirect('index')


def register(request):

   

    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            user = form.save(commit = False)

            user.save()
            print('user created')
            login(request, user)
            messages.success(request, 'registered! logged in!')
            return redirect('dashboard')
        else:
            messages.success(request, 'an error occurred')
            return redirect('register')
    else:
        form = Register()

    
    return render(request, 'Authentication/register.html', {'form': form})



  