from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import User

def users(request):
    users = User.objects.values()  # get all users
    users_list = list(users)
    return JsonResponse(users_list, safe=False)

def health_check(request):
    return HttpResponse("OK", status=200)