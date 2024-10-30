#django
def dj(alias_manager):
    print("______________Django")
    alias_manager.add_alias('dj_cl_migrations', 'find . -path "*/migrations/*.py" -not -name "__init__.py" -delete')
    alias_manager.add_alias('rm_python_cache', 'find . -type d -name "__pycache__" -exec rm -r {} +')
