from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cadastro_ong.views import cadastro_ong, login

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista_ong/', views.lista_ong, name='lista_ong'),
    #path('cadastro_enviado/', cadastro_enviado, name='cadastro_enviado'),
    #path('login/', login, name='login'),
    path('admin/login/', login, name='login'),
    #path('cadastro_pet/', cadastro_pet, name='cadastro_pet'),
    #path('pet_enviado/', pet_enviado, name='pet enviado'),
    path("lista_pets", views.lista_pets, name="lista_pets"),
    path("detalhes_pet/<int:pet_id>", views.detalhes_pet, name="detalhes_pet"),
    path("localizacao_pet/<int:pet_id>", views.localizacao_pet, name="localizacao_pet"),
    path('cadastro_ong/', cadastro_ong, name='cadastro_ong'),
    path('acessibilidade', views.acessibilidade, name='acessibilidade'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)