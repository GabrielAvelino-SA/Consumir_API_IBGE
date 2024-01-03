from django.urls import path
from consulta import views

urlpatterns = [
    path('', views.index, name='index')
]