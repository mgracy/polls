from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse('index')

def detail(request, id):
	return HttpResponse('detail')