import os
import subprocess
import argparse
from typing import List

class GitStatusChecker:
    def __init__(self, base_path: str):
        self.base_path = base_path

    def get_directories(self) -> List[str]:
        """Get a list of directories in the base path."""
        return [os.path.join(self.base_path, d) for d in os.listdir(self.base_path) 
                if os.path.isdir(os.path.join(self.base_path, d))]

    def execute_git_status(self, directory: str) -> str:
        """Execute `git status` in the given directory and return the output."""
        try:
            result = subprocess.run(['git', 'status'], cwd=directory, text=True, capture_output=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error executing git status in {directory}: {e}"

    def check_status(self) -> None:
        """Check git status for each directory."""
        directories = self.get_directories()
        for directory in directories:
            print(f"Checking status in: {directory}")
            status = self.execute_git_status(directory)
            print(status)

def main():
    parser = argparse.ArgumentParser(description="Check git status for directories in the given path.")
    parser.add_argument('path', type=str, help="The path to check for git status.")
    args = parser.parse_args()

    checker = GitStatusChecker(args.path)
    checker.check_status()

if __name__ == "__main__":
    main()
