from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
# def home(request):
#     data= {"NAME:-":"PRIYA ROY ",
#            "AGE:-":"26 ",
#            "MOB NO:-":"=234567890"
#            }
#     return JsonResponse(data)

def register(request):
    return render(request, 'register.html')