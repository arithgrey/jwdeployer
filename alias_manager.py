import os

class AliasManager:
    def __init__(self, bashrc_path=os.path.expanduser("~/.bashrc")):
        self.bashrc_path = bashrc_path

    def alias_exists(self, name):
        """Check if an alias already exists in the .bashrc file."""
        with open(self.bashrc_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith(f"alias {name}="):
                    return True
        return False

    def add_alias(self, name, command):
        if not self.alias_exists(name):
            alias_command = f"alias {name}='{command}'\n"
            with open(self.bashrc_path, 'a') as file:
                file.write(alias_command)
            print(f"Alias '{name}' añadido con éxito.")
        else:
            print(f"Alias '{name}' ya existe.")

    def reload_bashrc(self):
        """Reload the .bashrc file to apply changes."""
        os.system('exec bash')
        print("Archivo .bashrc recargado.")

alias_manager = AliasManager()

# Agregar alias
alias_manager.add_alias('jw_service', 'git clone git@github.com:arithgrey/jwdeployer.git && cd jwdeployer && python3 -m venv env && source env/bin/activate && pip install -r requirements.txt')
alias_manager.add_alias('jw_deployment', 'python deployment_to_kubernets.py')

# Recargar .bashrc
alias_manager.reload_bashrc()
