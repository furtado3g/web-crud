from django.shortcuts import render
from .models import produtos
# Create your views here.
def home(request):
    if(request.method == "GET"):
        try:
            Produtos = produtos.objects.all()
        except:
            raise Http404("forbiden page")
        context = {
            'listaDeProdutos' : Produtos
        }
        return render(request,'home.html',context)