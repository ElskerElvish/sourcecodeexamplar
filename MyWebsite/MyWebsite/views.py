from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request, "index.html")

def home(a):
	return HttpResponse("<h1>Shubham</h1>")