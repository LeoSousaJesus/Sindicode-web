from django.urls import path
from associados import views
from associados.views import index

urlpatterns = [
    path('cadastro', index),
]