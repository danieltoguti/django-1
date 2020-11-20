from django.shortcuts import render
from .models import Produto


def index(request):
    produtos = Produto.objects.all()

    context = {
        'loja' : 'Em Casa com Estilo',
        'eslogam' : 'De bem com você',
        'venda' : 'Encontre o modelo que combine com você',
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    prod = Produto.objects.get(id=pk)
    context = {
        'produto': prod,
    }

    return render(request, 'produto.html', context)

