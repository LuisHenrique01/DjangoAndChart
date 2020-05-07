from django.shortcuts import render, redirect
from .models import CasosPorCidadePiaui

# Create your views here.
def index(request):
    base = {}
    base['brasil'] = [['br-sp', 0],
                      ['br-ma', 1],
                      ['br-pa', 2],
                      ['br-sc', 3],
                      ['br-ba', 4],
                      ['br-ap', 5],
                      ['br-ms', 6],
                      ['br-mg', 7],
                      ['br-go', 8],
                      ['br-rs', 9],
                      ['br-to', 10],
                      ['br-pi', 11],
                      ['br-al', 12],
                      ['br-pb', 13],
                      ['br-ce', 14],
                      ['br-se', 15],
                      ['br-rr', 16],
                      ['br-pe', 17],
                      ['br-pr', 18],
                      ['br-es', 19],
                      ['br-rj', 20],
                      ['br-rn', 21],
                      ['br-am', 22],
                      ['br-mt', 23],
                      ['br-df', 24],
                      ['br-ac', 25],
                      ['br-ro', 26]]
    base['piaui'] = CasosPorCidadePiaui.objects.all()
    return render(request, 'index.html', base)


def importar(request):
    file = request.FILES['arquivo'].read().decode('utf-8')
    cidades = file.replace("\r","").split("\n")
    book = []
    for linha in cidades:
        try:
            nome, idibge, casos, mortes = linha.split(',')
            book.append(CasosPorCidadePiaui(name=nome, idIBGE=idibge, casos=casos, obitos=mortes))
        except ValueError:
            pass
    CasosPorCidadePiaui.objects.bulk_create(book)
        
    return redirect('index')
