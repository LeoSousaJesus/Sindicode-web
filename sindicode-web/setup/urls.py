from django.contrib import admin
from django.urls import path
from django.urls import include

import associados

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('noticias.urls')),
    path('',include('associados.urls')),
]

