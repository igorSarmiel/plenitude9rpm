from django.urls import path
from . import views

app_name = "material"

urlpatterns=[
    path('listar/', views.listar_material, name='listar'),
    path('cadastrar/', views.cadastrar_material, name='cadastrar'),
    path('editar/<int:id>', views.editar_material, name='editar'),
    path('deletar/<int:id>', views.deletar_material, name='deletar'),
    path('liberar_material/<int:id_mat>/<int:id_resp>', views.liberar_material, name='liberar_material'),
    path('locacoes_ativas/', views.locacoes_ativas, name='locacoes_ativas'),
]