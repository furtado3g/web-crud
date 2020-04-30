from django.shortcuts import render
from .models import produtos
from django.forms import ModelForm
from django.http import Http404,JsonResponse
from django.views.decorators.csrf import csrf_protect,ensure_csrf_cookie,csrf_exempt
# Create your views here.
class ProductForm(ModelForm):
    class Meta:
        model = produtos
        fields = ['nome','cod_barras','valor']

@csrf_exempt
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
    if(request.method == 'POST'):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request,'/')
        else:
            context = {
                'erros' : 'Erro ao preencher'
            }
            return render(request,'home.html',context)

@csrf_exempt
def atualizar(request,pk):
    if request.method == 'GET' :
        try:
            produto = produtos.objects.filter(pk=pk)
        except:
            raise Http404("forbiden page")
        context = {
            'produtos' : produto
        }
        return render(request,'modalProduto.html',context)
    elif request.method == 'POST' :
        user= get_object_or_404(User, pk=pk) 
        form = UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save( )
            return redirect(request,'/')
        else:
            context = {
                'erros' : 'Erro ao editar produto'
            }
            return render(request,'home.html',context)
    elif request.method == "DELETE":
        User.objects.filter(pk).delete()
        return redirect(request,'/')

