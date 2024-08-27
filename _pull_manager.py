import os
import subprocess
from abc import ABC, abstractmethod

# Interface Segregation: Definimos una interfaz para GitService
class GitService(ABC):
    @abstractmethod
    def check_for_updates(self, directory: str) -> bool:
        pass

    @abstractmethod
    def pull_updates(self, directory: str) -> None:
        pass

# Implementación concreta que sigue la interfaz GitService
class GitHubService(GitService):
    def check_for_updates(self, directory: str) -> bool:
        # Check for updates using git fetch
        subprocess.run(
            ["git", "fetch"],
            cwd=directory,
            capture_output=True,
            text=True
        )
        # Check if there are any changes
        result_diff = subprocess.run(
            ["git", "diff", "HEAD", "origin/main"],
            cwd=directory,
            capture_output=True,
            text=True
        )
        return bool(result_diff.stdout)

    def pull_updates(self, directory: str) -> None:
        # Pull the latest changes from the main branch
        result_pull = subprocess.run(
            ["git", "pull", "origin", "main"],
            cwd=directory,
            capture_output=True,
            text=True
        )
        if result_pull.returncode == 0:
            print(f"Successfully pulled updates in {directory}")
        else:
            print(f"Failed to pull updates in {directory}: {result_pull.stderr}")

# Single Responsibility: Clase para recorrer directorios
class DirectoryScanner:
    def __init__(self, path: str, git_service: GitService):
        self.path = path
        self.git_service = git_service

    def scan_and_update(self):
        for root, dirs, _ in os.walk(self.path):
            for directory in dirs:
                full_path = os.path.join(root, directory)
                if os.path.isdir(os.path.join(full_path, ".git")):  # Verifica si es un repositorio git
                    print(f"Checking for updates in {full_path}")
                    if self.git_service.check_for_updates(full_path):
                        print(f"Changes detected in {full_path}")
                        self.git_service.pull_updates(full_path)

# Dependency Inversion: Usamos la abstracción GitService en lugar de una clase concreta
def main():
    path_to_services = "/home/_enid_service/services"
    git_service = GitHubService()
    scanner = DirectoryScanner(path_to_services, git_service)
    scanner.scan_and_update()

if __name__ == "__main__":
    main()
