from django.shortcuts import render
from .models import Produto

# Create your views here.
def index(request):
    base = {}
    base['produtos'] = Produto.objects.all().order_by('preco')
    base['pizza'] = [int(round(j.preco/sum([i.preco for i in base['produtos']]), 2)*100) for j in base['produtos']]
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
    return render(request, 'index.html', base)