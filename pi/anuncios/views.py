from django.shortcuts import render

def index(request):
    return render(request, 'anuncios/index.html')

def produtos(request):
    return render(request, 'anuncios/produtos.html')

def servicos(request):
    return render(request, 'anuncios/servicos.html')
