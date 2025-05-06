import os
import sys

def main():
    """Função principal para executar tarefas administrativas do Django."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zure_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Não foi possível importar Django. Certifique-se de que ele está instalado "
            "e disponível no ambiente virtual ativo."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()