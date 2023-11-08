#!/bin/bash

###### README ######
###############################################################################################################################
## Por Thandara Felix - thandara_louise@hotmail.com 07/11/2023                                                                ##
## Objetivo :  Criar ambiente de producao virtualizado em nuvem para a aplicacao petmatch - Requisito PI II                   ##
## GERENCIADO django no /etc/system/systemd/django.service                                                                    ##
## Script para inicialização do django no boot, depende que o nginx esteja instalado e a pasta copiada para o /etc , arquivo  ##
## django.service esteja no path correto e systemctl daemon-reload tenha sido executa conforme documentacao                   ##
## Para subir o ambiente execute: sudo systemctl start django  e este script será executado                                   ##
################################################################################################################################

## Variaveis
PROJECT="/home/petmatch/petmatch-django/"
VIRTUALENV="/home/petmatch/petmatch-django/venv/bin/activate"
PYTHON="/home/petmatch/petmatch-django/venv/bin/python3"
GUNICORN="/home/petmatch/petmatch-django/venv/gunicorn"
NGINX="systemctl start nginx"

## Ativar ambiente virtual
source /home/petmatch/petmatch-django/venv/bin/activate

##Coletando arquivos estáticos e estilos
$PYTHON manage.py collectstatic --noinput

##Criando campos na base de dados configuradas no django-admin
$PYTHON manage.py migrate

##Inicia o servidor Django - porta default 8000
$PYTHON manage.py runserver

##Inicia Gunicorn - Intermediador para APIs em Python
$GUNICORN -c $PROJECT/setup/gunicorn.py petmatch.wsgi

##Inicia o Nginx - Para seguranca
$NGINX

## Com este script é esperado que a aplicacao funcione rodando na porta 8000 e o Gunicorn 'assista' as requisicoes

