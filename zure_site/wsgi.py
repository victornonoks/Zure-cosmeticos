# wsgi.py - Deploy
import os 
from django.core.wsgi import get_wsgi_application
# Definindo o módulo de configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zure_site.settings')

# Criando a aplicação WSGI
application = get_wsgi_application()