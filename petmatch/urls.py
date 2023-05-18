from django.urls import path
from petmatch.views import cadastro_ong, cadastro_enviado, cadastro_pet, login, index, pet_enviado

urlpatterns = [
    path('', index, name='index'),
    path('cadastro_ong/', cadastro_ong, name='cadastro_ong'),
    path('cadastro_enviado/', cadastro_enviado, name='cadastro_enviado'),
    path('login/', login, name='login'),
    path('cadastro_pet/', cadastro_pet, name='cadastro_pet'),
    path('pet_enviado/', pet_enviado, name='pet enviado')
]