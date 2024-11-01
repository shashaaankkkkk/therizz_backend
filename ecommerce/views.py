from django.http import response , HttpResponse
 
from django.shortcuts import render
def home(request):
    return HttpResponse("<h1>hello this is rizz backend</h1>")