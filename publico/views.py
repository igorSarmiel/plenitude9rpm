from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import Publico_form, Dependentes_form, Obs_publico_form, Obs_dependente_form, Locacao_form
from .models import Publico, Dependentes, Locacao
from django.apps import apps
from datetime import datetime
from math import floor

@login_required
def cadastrar_publico(request):
    if request.method == "POST":
        publico_form = Publico_form(request.POST)
        if publico_form.is_valid():
            publico_form.save()
            return redirect('publico:listar')
        else:
            return render(request,'publico/cadastrar_publico.html', {'publico_form':Publico_form(request.POST)})
    else:
        publico_form = Publico_form()
        return render(request,'publico/cadastrar_publico.html', {'publico_form':publico_form})


@login_required
def listar_publico(request):
    publicos = Publico.objects.all()
    return render(request, 'publico/listar_publico.html', {'publicos':publicos, })


@login_required
def editar_publico(request, id):
    dados = Publico.objects.get(pk=id)
    publico_form_editar = Publico_form(request.POST or None, instance=dados)
    if request.method == "POST":
        if publico_form_editar.is_valid():
            publico_form_editar.save()
            return redirect('/publico/ficha/'+str(id))
        else:
            return render(request, 'publico/cadastrar_publico.html', {'publico_form': publico_form_editar})
    else:
        return render(request, 'publico/cadastrar_publico.html',{'publico_form':publico_form_editar,} )


@login_required
def deletar(request, id):
    registro = get_object_or_404(Publico, pk=id)
    registro.delete()
    return redirect('publico:listar')

def idade(nasc):
    hoje = datetime.now().date()
    dif = hoje - nasc
    return floor(dif.days/365)


@login_required
def ficha(request, id):
    dados = Publico.objects.get(pk=id)
    dependentes = Dependentes.objects.filter(responsavel=id)
    locacoes = Locacao.objects.filter(locador=id)
    locados = []
    material = apps.get_model(app_label="material", model_name="Material")

    for loc in locacoes:
        m = material.objects.get(pk=loc.material.id)
        if m.locado == True:
            locados.append(loc)

    return render(request, 'publico/ficha.html',{'dados':dados, 'dependentes':dependentes,
                                                 "locacoes":locados, "idade":idade(dados.data_nascimento)})


@login_required
def cad_dependentes(request, id):
    responsavel = Publico.objects.get(pk=id)
    if request.method == "POST":
        dependente_form = Dependentes_form(request.POST)
        if dependente_form.is_valid():
            dependente_form.save()
            return redirect('/publico/ficha/'+str(id))
        else:
            return render(request, 'publico/cadastrar_dependente.html',
                          {'dependente_form':dependente_form, 'responsavel':responsavel})
    else:
        dependente_form = Dependentes_form(initial={"responsavel":responsavel.id},)
        return render(request, 'publico/cadastrar_dependente.html',
                      {'dependente_form':dependente_form, 'responsavel':responsavel})


@login_required
def deletar_dependente(request, id, resp):
    depentende = get_object_or_404(Dependentes, pk=id)
    depentende.delete()
    return redirect('/publico/ficha/'+str(resp))


@login_required
def editar_dependentes(request, id, resp):
    dados = Dependentes.objects.get(pk=id)
    responsavel = Publico.objects.get(pk=resp)
    dependente_form_editar = Dependentes_form(request.POST or None, instance=dados)
    if request.method == "POST":
        if dependente_form_editar.is_valid():
            dependente_form_editar.save()
            return redirect('/publico/ficha/'+str(resp))
        else:
            return render(request, 'publico/cadastrar_dependente.html',
                          {'dependente_form': dependente_form_editar,
                           'responsavel':responsavel,})
    else:
        return render(request, 'publico/cadastrar_dependente.html',
                      {'dependente_form': dependente_form_editar,
                       'responsavel':responsavel, })


@login_required
def obs_publico(request, id):
    dados = Publico.objects.get(pk=id)
    obs_publico_form = Obs_publico_form(request.POST or None, instance=dados)
    if request.method == "POST":
        if obs_publico_form.is_valid():
            obs_publico_form.save()
            return ficha(request, id)
        else:
            return render(request, 'publico/obs_publico.html',
                          {'obs_publico_form': obs_publico_form,
                           'dados': dados})
    else:
        return render(request, 'publico/obs_publico.html',
                  {'obs_publico_form':obs_publico_form,
                   'dados':dados})


@login_required
def obs_dependente(request, id, resp):
    dependente = Dependentes.objects.get(pk=id)
    responsavel = Publico.objects.get(pk=resp)
    obs_dependente_form = Obs_dependente_form(request.POST or None, instance=dependente)
    if request.method == "POST":
        if obs_dependente_form.is_valid():
            obs_dependente_form.save()
            return redirect('/publico/ficha/'+str(resp))
        else:
            return render(request, 'publico/obs_dependente.html',
                          {'obs_dependente_form': obs_dependente_form, 'responsavel': responsavel})
    else:
        return render(request, 'publico/obs_dependente.html',
                  {'obs_dependente_form':obs_dependente_form, 'responsavel':responsavel })


@login_required
def locar_material(request, id):
    if request.method == "POST":
        locacao_form = Locacao_form(request.POST)
        if locacao_form.is_valid():
            locacao_form.save()
            Material = apps.get_model(app_label="material", model_name="Material")
            material = Material.objects.get(pk=locacao_form['material'].value())
            material.locado = True
            material.locador = locacao_form['locador'].value()
            material.save()
            return redirect('/publico/ficha/'+str(id))
        else:
            locador = Publico.objects.get(pk=id)
            return render(request, 'publico/locar_material.html', {'locacao_form': locacao_form,
                                                                   'locador': locador,})
    else:
        locador = Publico.objects.get(pk=id)
        locacao_form = Locacao_form(initial={'locador':locador.id,}, instance=locador)
        return render(request, 'publico/locar_material.html', {'locacao_form':locacao_form,
                                                                    'locador':locador, })