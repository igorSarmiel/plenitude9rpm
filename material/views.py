from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Material
from .forms import Material_form
from django.apps import apps
from datetime import datetime

@login_required
def listar_material(request):
    materiais = Material.objects.all()
    return render(request, 'material/listar_material.html', {'materiais':materiais})

@login_required
def cadastrar_material(request):
    if request.method == "POST":
        material_form = Material_form(request.POST)
        if material_form.is_valid():
            material_form.save()
            return redirect('/material/listar')
        else:
            return render(request, 'material/cadastrar_material.html', {'material_form':material_form})
    else:
        return render(request, 'material/cadastrar_material.html', {'material_form': Material_form})

@login_required
def editar_material(request, id):
    material = Material.objects.get(pk=id)
    material_form = Material_form(request.POST or None, instance=material)
    if request.method == "POST":
        if material_form.is_valid():
            material_form.save()
            return redirect('/material/listar')
        else:
            return render(request, 'material/cadastrar_material.html',context={'material_form':material_form})
    else:
        return render(request, 'material/cadastrar_material.html', context={'material_form': material_form})

@login_required
def deletar_material(request, id):
    material = get_object_or_404(Material, pk=id)
    material.delete()
    return redirect('/material/listar/')


@login_required
def liberar_material(request, id_mat, id_resp):
    material = get_object_or_404(Material, pk=id_mat)
    material.locado = False
    material.save()
    return redirect("/publico/ficha/"+str(id_resp))

def contagem_dias(dia_locado):
    hoje = datetime.now().date()
    dif = hoje - dia_locado
    return dif.days


@login_required
def locacoes_ativas(request):
    locacoes = apps.get_model(app_label="publico", model_name="Locacao")
    ativos = Material.objects.filter(locado=True)
    lista_ativos = []
    for ativo in ativos:
        locados = locacoes.objects.filter(material=ativo.id)
        l = len(locados)
        loc = locados[l-1]
        lista_ativos.append((ativo, loc.locador.id, loc.locador, contagem_dias(loc.data_locado)))

    return render(request, 'material/locacoes_ativas.html', {"ativos":lista_ativos, })


def contagem_material(request):
    #locacoes = apps.get_model(app_label="publico", model_name="Locacao")
    tipos = ['ANDADOR', 'MULETA', 'CADEIRA_RODAS','CADEIRA_BANHO', 'CAMA',
              'COLCHAO', 'TIPOIA', 'COLAR_CERVICAL', 'BOTA_ORTOPEDICA', 'OUTROS', ]
    total = 0
    dados = []
    for tipo in tipos:
        #conta a quantidade de cada tipo de material
        subtotal = Material.objects.filter(tipo=tipo).count()
        icon = "img/{}.jpg".format(tipo)
        dados.append([tipo, subtotal, icon])
        total += subtotal
    return render(request, 'material/contagem_material.html', {"dados":dados, "total":total})