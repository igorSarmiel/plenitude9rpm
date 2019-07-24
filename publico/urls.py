from django.urls import path
from . import views

app_name="publico"

urlpatterns=[
    path('cadastrar/', views.cadastrar_publico, name='cadastrar'),
    path('listar/', views.listar_publico, name='listar'),
    path('editar/<int:id>', views.editar_publico, name='editar'),
    path('ficha/<int:id>', views.ficha, name='ficha'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
    path('cad_dependentes/<int:id>', views.cad_dependentes, name='cad_dependentes'),
    path('deletar_dependente/<int:id>/<int:resp>', views.deletar_dependente, name='del_dependente'),
    path('editar_dependentes/<int:id>/<int:resp>', views.editar_dependentes, name='editar_dependentes'),
    path('editar_obs_publico/<int:id>', views.obs_publico, name='obs_publico'),
    path('obs_dependente/<int:id>/<int:resp>', views.obs_dependente, name='obs_dependente'),
    path('locar_material/<int:id>', views.locar_material, name='locar'),

]