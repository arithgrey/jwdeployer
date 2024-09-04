import os
from aliases import add_aliases
class AliasManager:
    def __init__(self, bashrc_path=os.path.expanduser("~/.bashrc")):
        self.bashrc_path = bashrc_path

    def alias_exists(self, name):
        """Check if an alias already exists in the .bashrc file and return its line number."""
        with open(self.bashrc_path, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if line.startswith(f"alias {name}="):
                    return i
        return None

    def add_alias(self, name, command):
        alias_command = f"alias {name}='{command}'\n"
        alias_line = self.alias_exists(name)

        if alias_line is not None:
            # Update the existing alias
            with open(self.bashrc_path, 'r') as file:
                lines = file.readlines()
            lines[alias_line] = alias_command
            with open(self.bashrc_path, 'w') as file:
                file.writelines(lines)
            print(f"Alias '{name}' actualizado con éxito.")
        else:
            # Add new alias
            with open(self.bashrc_path, 'a') as file:
                file.write(alias_command)
            print(f"Alias '{name}' añadido con éxito.")

    def reload_bashrc(self):
        """Reload the .bashrc file to apply changes."""
        os.system('exec bash')
        print("Archivo .bashrc recargado.")
        
# Crear una instancia de AliasManager
alias_manager = AliasManager()
add_aliases(alias_manager)
alias_manager.reload_bashrc()
