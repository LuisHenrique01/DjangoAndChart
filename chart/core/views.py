from django.shortcuts import render
from .models import Produto

# Create your views here.
def index(request):
    base = {}
    base['produtos'] = Produto.objects.all()
    base['pizza'] = [int(round(j.preco/sum([i.preco for i in base['produtos']]), 2)*100) for j in base['produtos']]
    return render(request, 'index.html', base)