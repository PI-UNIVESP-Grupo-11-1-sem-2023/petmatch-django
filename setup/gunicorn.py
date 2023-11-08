command = '/home/petmatch/petmatch-django/venv/bin/gunicorn'
pythonpath = '/home/petmatch/petmatch-django'
bind = '172.31.32.175:8000'
workers = 3
module = 'petmatch.wsgi'

##INTERMEDIADOR DE APIS EM PYTHON, O IP DO BIND DEVE SER CONFIGURADO DE ACORDO COM O IP DE LOCALHOST
