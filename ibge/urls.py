from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # minhas rotas
    path('ibge/', include("consulta.urls")),
]
