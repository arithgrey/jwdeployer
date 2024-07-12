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
            result = subprocess.run(["docker-compose", "up", "-d"])
            if result.returncode != 0:
                print(f"Error executing docker-compose up in {compose_file}.")

if __name__ == "__main__":
    
    print("al final del servicio indica en que directorio se encuentran los docker-compose ejemplo jw_docker_compose_runner_service /home/arith")
    if len(sys.argv) < 2:
        print("Usage: python script.py <base_directory>")
        sys.exit(1)
    
    base_directory = sys.argv[1]
    if not os.path.isdir(base_directory):
        print(f"The directory {base_directory} does not exist.")
        sys.exit(1)
    
    runner = DockerComposeRunner(base_directory)
    runner.run_docker_compose_up()