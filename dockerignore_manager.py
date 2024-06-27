import os
from docker_entries import entries

class DockerignoreManager:
    def __init__(self, dockerignore_path="../.dockerignore"):
        self.dockerignore_path = os.path.join(os.getcwd(), dockerignore_path)
        self.ensure_dockerignore_exists()

    def ensure_dockerignore_exists(self):
        """Ensure the .dockerignore file exists."""
        if not os.path.exists(self.dockerignore_path):
            open(self.dockerignore_path, 'w').close()
            print(f"Archivo .dockerignore creado en {self.dockerignore_path}")

    def entry_exists(self, entry):
        """Check if an entry already exists in the .dockerignore file."""
        with open(self.dockerignore_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.strip() == entry:
                    return True
        return False

    def add_entry(self, entry):
        if self.entry_exists(entry):
            print(f"Entry '{entry}' ya existe en el archivo .dockerignore.")
        else:
            with open(self.dockerignore_path, 'a') as file:
                file.write(f"{entry}\n")
            print(f"Entry '{entry}' añadido con éxito al archivo .dockerignore.")

# Crear una instancia de dockerignoreManager
dockerignore_manager = DockerignoreManager()

# Agregar entradas al archivo .dockerignore
for entry in entries:
    dockerignore_manager.add_entry(entry)
