from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Exp, Token, Income, User
from datetime import datetime


@csrf_exempt
def submit_income(request):
    """user submit an income"""
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()

    Income.objects.create(user=this_user, amount=request.POST['amount'],
                          text=request.POST['text'], date=date)
    return JsonResponse({
        'status ': 'ok',
    }, encoder=json.JSONEncoder)


# Create your views here.
@csrf_exempt
def submit_exp(request):
    """user submit an expense"""
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()

    Exp.objects.create(user=this_user, amount=request.POST['amount'],
                       text=request.POST['text'], date=date)
    print(request.POST)
    return JsonResponse({
        'status ': 'ok',
    }, encoder=json.JSONEncoder)
