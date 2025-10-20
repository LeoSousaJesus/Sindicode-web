from django.shortcuts import render
from django.http import HttpResponse

# função
# se def dentro da classe = metodo
# se def fora da classe = função
def index(request):
    return HttpResponse("<h1><marquee>Alô Django</marquee></h1>")

# Create your views here.
