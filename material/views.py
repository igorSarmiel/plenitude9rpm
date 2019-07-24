from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Material
from .forms import Material_form

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
