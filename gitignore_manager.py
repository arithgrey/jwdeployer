import os
from gitignore_entries import entries  # Importar las entradas desde gitignore_entries.py

class GitignoreManager:
    def __init__(self, gitignore_path="../.gitignore"):
        self.gitignore_path = os.path.join(os.getcwd(), gitignore_path)
        self.ensure_gitignore_exists()

    def ensure_gitignore_exists(self):
        """Ensure the .gitignore file exists."""
        if not os.path.exists(self.gitignore_path):
            open(self.gitignore_path, 'w').close()
            print(f"Archivo .gitignore creado en {self.gitignore_path}")

    def entry_exists(self, entry):
        """Check if an entry already exists in the .gitignore file."""
        with open(self.gitignore_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.strip() == entry:
                    return True
        return False

    def add_entry(self, entry):
        if self.entry_exists(entry):
            print(f"Entry '{entry}' ya existe en el archivo .gitignore.")
        else:
            with open(self.gitignore_path, 'a') as file:
                file.write(f"{entry}\n")
            print(f"Entry '{entry}' añadido con éxito al archivo .gitignore.")

# Crear una instancia de GitignoreManager
gitignore_manager = GitignoreManager()

# Agregar entradas al archivo .gitignore
for entry in entries:
    gitignore_manager.add_entry(entry)
