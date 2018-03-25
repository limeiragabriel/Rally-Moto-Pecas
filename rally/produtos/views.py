from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import ProdutoForm, UserForm
from .models import Produto

from django.views import generic
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse

from django.shortcuts import redirect

#AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def create_produto(request):
    if not request.user.is_authenticated():
        return render(request, 'produtos/login.html')
    else:
        form = ProdutoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.user = request.user
            produto.imagem = request.FILES['imagem']
            file_type = produto.imagem.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'produto': produto,
                    'form': form,
                    'error_message': 'Imagem deve ser PNG, JPG, ou JPEG',
                }
                return render(request, 'produtos/create_produto.html', context)
            produto.save()
            return render(request, 'produtos/detail.html', {'produto': produto})
        context = {
            "form": form,
        }
        return render(request, 'produtos/create_produto.html', context)


def delete_produto(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    produto.delete()
    produtos = Produto.objects.filter(user=request.user)
    return render(request, 'produtos/index.html', {'produtos': produtos})


def detail(request, produto_id):
    if not request.user.is_authenticated():
        return render(request, 'produtos/login.html')
    else:
        user = request.user
        produto = get_object_or_404(Produto, pk=produto_id)
        return render(request, 'produtos/detail.html', {'produto': produto, 'user': user})


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'produtos/login.html')
    else:
        produtos = Produto.objects.filter(user=request.user)
        query = request.GET.get("q")
        if query:
            produtos = produtos.filter(
                Q(pk__icontains=query) |
                Q(nome__icontains=query)
            ).distinct()
            return render(request, 'produtos/index.html', {
                'produtos': produtos,
            })
        else:
            return render(request, 'produtos/index.html', {'produtos': produtos})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'produtos/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                produtos = Produto.objects.filter(user=request.user)
                return render(request, 'produtos/index.html', {'produtos': produtos})
            else:
                return render(request, 'produtos/login.html', {'error_message': 'Conta desativada'})
        else:
            return render(request, 'produtos/login.html', {'error_message': 'Login invalido'})
    return render(request, 'produtos/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                produtos = Produto.objects.filter(user=request.user)
                return render(request, 'produtos/index.html', {'produtos': produtos})
    context = {
        "form": form,
    }
    return render(request, 'produtos/register.html', context)


class ProdutoUpdate(UpdateView):
    model = Produto
    fields = ['nome','valor','estoque','imagem']
    
    def get_success_url(self):
        view_name = 'produtos:detail'
        return reverse(view_name, kwargs={'produto_id': self.object.id})


def vender_produto(request,pk):
    produto_id = int(request.POST['produto_id'])
    produto = Produto.objects.get(id=produto_id)
    user = request.user

    context = {'produto': produto,'user': user , 'succes_message': 'Venda realizada com sucesso.'}

    if request.method == 'POST':
        qtdRequest = request.POST['qtd']
        
        if qtdRequest == "":
            context = {'produto': produto,'user': user, 'error_message': 'Entrada inválida.',}
            return render(request, 'produtos/detail.html', context )

        else:
            qtd = int(float(qtdRequest))
            if produto.estoque >= qtd:
                produto.estoque = produto.estoque - qtd
                produto.save()
            else:
                context = {'produto': produto,'user': user,'error_message': 'Estoque insuficiente.',}

    return render(request, 'produtos/detail.html', context)