#django
def dj(alias_manager):
    print("______________Django")
    alias_manager.add_alias('dj_cl_migrations', 'find . -path "*/migrations/*.py" -not -name "__init__.py" -delete')