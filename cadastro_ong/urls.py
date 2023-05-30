from django.urls import path
from cadastro_ong.views import cadastro_ong, cadastro_enviado, login, pets_matilhadaba, pets_lartemporariox
from petmatch.views import lista_ong, lista_pet, index

urlpatterns = [
    path('cadastro_ong/login/', login, name='login'),
    path('cadastro_ong/', cadastro_ong, name='cadastro_ong'),
    path('cadastro_enviado/', cadastro_enviado, name='cadastro_enviado'),
    path('login/pets_matilhadaba/', pets_matilhadaba, name='pets_matilhadaba'),
    path('login/pets_lartemporariox', pets_lartemporariox, name='pets_lartemporariox'),
]