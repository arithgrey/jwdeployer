#pip, python, env, venv
def pip(alias_manager):
    print("______________PIP")
    alias_manager.add_alias('pip_new_requirements','pip freeze | grep -Fxv -f requirements.txt >> requirements.txt')
    alias_manager.add_alias('rm_env','rm -rf env/')