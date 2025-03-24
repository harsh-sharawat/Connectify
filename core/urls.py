
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('au/',include('Authentication.urls')),
    path('dashboard/' ,views.dashboard , name = 'dashboard'),
    
]
