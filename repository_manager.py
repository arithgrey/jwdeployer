import os
import importlib.util
from git import Repo

class RepositoryManager:
    def clone_or_update_repo(self, repo_url: str, target_path: str):
        pass

class GitRepositoryManager(RepositoryManager):
    def clone_or_update_repo(self, repo_url: str, target_path: str):
        if os.path.exists(target_path):
            self._update_repo(target_path)
        else:
            self._clone_repo(repo_url, target_path)

    def _clone_repo(self, repo_url: str, target_path: str):
        print(f"Cloning repository {repo_url} to {target_path}")
        Repo.clone_from(repo_url, target_path)
        print("Clone completed.")

    def _update_repo(self, target_path: str):
        print(f"Updating repository at {target_path}")
        repo = Repo(target_path)
        origin = repo.remotes.origin
        origin.pull()
        print("Update completed.")

class RepositoryProcessor:
    def __init__(self, repo_manager: RepositoryManager):
        self.repo_manager = repo_manager

    def process_repositories(self, repo_urls: list, base_path: str):
        for repo_url in repo_urls:
            repo_name = repo_url.split('/')[-1].replace('.git', '')
            target_path = os.path.join(base_path, repo_name)
            self.repo_manager.clone_or_update_repo(repo_url, target_path)

def load_config(module_name: str) -> dict:
    spec = importlib.util.spec_from_file_location(module_name, f"{module_name}.py")
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
    return config

def main():
    config = load_config('repository_config')
    repo_urls = config.repositories
    base_path = '../services'

    repo_manager = GitRepositoryManager()
    processor = RepositoryProcessor(repo_manager)
    processor.process_repositories(repo_urls, base_path)

if __name__ == "__main__":
    main()
