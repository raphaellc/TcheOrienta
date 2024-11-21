from django.shortcuts import render, redirect, get_object_or_404
from .models import Estabelecimento
from .forms import EstabelecimentoForm  # Adicione um arquivo forms.py para os formulários
from django.views.decorators.csrf import csrf_exempt
# Listar estabelecimentos
def listar_estabelecimentos(request):
    estabelecimentos = Estabelecimento.buscar_todos_estabelecimentos()
    return render(request, 'estabelecimentos/listar.html', {'estabelecimentos': estabelecimentos})

# Criar estabelecimento
@csrf_exempt
def criar_estabelecimento(request):
    if request.method == 'POST':
        form = EstabelecimentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_estabelecimentos')
    else:
        form = EstabelecimentoForm()
    return render(request, 'estabelecimentos/criar.html', {'form': form})

# Editar estabelecimento
def editar_estabelecimento(request, id):
    estabelecimento = get_object_or_404(Estabelecimento, id=id)
    if request.method == 'POST':
        form = EstabelecimentoForm(request.POST, request.FILES, instance=estabelecimento)
        if form.is_valid():
            form.save()
            return redirect('listar_estabelecimentos')
    else:
        form = EstabelecimentoForm(instance=estabelecimento)
    return render(request, 'estabelecimentos/editar.html', {'form': form})

# Deletar estabelecimento
def deletar_estabelecimento(request, id):
    estabelecimento = get_object_or_404(Estabelecimento, id=id)
    if request.method == 'POST':
        estabelecimento.delete()
        return redirect('listar_estabelecimentos')
    return render(request, 'estabelecimentos/deletar.html', {'estabelecimento': estabelecimento})
