from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def second(request):
    return HttpResponse('this is second app2')
def second_app2(request):
    return HttpResponse('this is second_app2')
