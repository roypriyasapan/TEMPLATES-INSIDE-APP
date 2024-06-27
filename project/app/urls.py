from django.urls import path,include
from .views import register
from app import views

urlpatterns = [
    path('register/',views.register)
    #path('home/',views.home)
    
]