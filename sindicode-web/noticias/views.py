from django.shortcuts import render
from django.http import HttpResponse

# função
# se def dentro da classe = metodo
# se def fora da classe = função
def index(request):
    return render(request, 'index.html')

# Create your views here.
