from django.shortcuts import render
import requests

def index(request):
    api = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/CE/municipios"
    requisicao = requests.get(api)

    try:
        lista = requisicao.json()
    except ValueError:
        print("A resposta não chegou com o formato esperado.")

    dicionario = {}
    for indice, valor in enumerate(lista):
        dicionario[indice] = valor

    contexto = {
        "municipios": dicionario
    }

    return render(request, "index.html", contexto)