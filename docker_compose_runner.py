import os
import subprocess
import sys

class DockerComposeRunner:
    def __init__(self, base_directory):
        self.base_directory = base_directory
    
    def find_docker_compose_files(self):
        docker_compose_files = []
        for root, dirs, files in os.walk(self.base_directory):
            if 'docker-compose.yml' in files:
                docker_compose_files.append(os.path.join(root, 'docker-compose.yml'))
        return docker_compose_files
    
    def run_docker_compose_up(self):
        docker_compose_files = self.find_docker_compose_files()
        if not docker_compose_files:
            print("No docker-compose.yml files found.")
            return
        
        for compose_file in docker_compose_files:
            print(f"Running docker-compose up in {compose_file}...")
            os.chdir(os.path.dirname(compose_file))
            result = subprocess.run(["/usr/local/bin/docker-compose", "up", "-d"])
            if result.returncode != 0:
                print(f"Error executing docker-compose up in {compose_file}.")
            else:
                print(f"Successfully ran docker-compose up in {compose_file}")
        
        return docker_compose_files

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <base_directory>")
        sys.exit(1)
    
    base_directory = sys.argv[1]
    if not os.path.isdir(base_directory):
        print(f"The directory {base_directory} does not exist.")
        sys.exit(1)
    
    runner = DockerComposeRunner(base_directory)
    docker_compose_files = runner.run_docker_compose_up()
    
    if docker_compose_files:
        print("Docker Compose files found and executed in the following directories:")
        for compose_file in docker_compose_files:
            print(os.path.dirname(compose_file))
    else:
        print("No Docker Compose files were found or executed.")
