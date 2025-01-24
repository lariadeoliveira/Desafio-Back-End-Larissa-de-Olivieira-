from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/autenticacao/', include('meu_projeto.apps.autenticacao.urls')),
]