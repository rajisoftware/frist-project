from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse('this is first app1')
def second_app1(request):
    return HttpResponse('this is second app1')
