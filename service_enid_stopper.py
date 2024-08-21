import os
import subprocess
import sys
import logging

class DockerComposeStopper:
    def __init__(self, base_directory, docker_compose_path="/usr/bin/docker-compose"):
        self.base_directory = base_directory
        self.docker_compose_path = docker_compose_path
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def find_docker_compose_files(self):
        docker_compose_files = []
        for root, dirs, files in os.walk(self.base_directory):
            if 'docker-compose.yml' in files:
                docker_compose_files.append(os.path.join(root, 'docker-compose.yml'))
        return docker_compose_files
    
    def run_docker_compose_stop(self):
        docker_compose_files = self.find_docker_compose_files()
        if not docker_compose_files:
            logging.warning("No docker-compose.yml files found.")
            return
        
        for compose_file in docker_compose_files:
            logging.info(f"Running docker-compose stop in {compose_file}...")
            os.chdir(os.path.dirname(compose_file))
            result = subprocess.run([self.docker_compose_path, "stop"])
            if result.returncode != 0:
                logging.error(f"Error executing docker-compose stop in {compose_file}.")
            else:
                logging.info(f"Successfully ran docker-compose stop in {compose_file}")
        
        return docker_compose_files

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <base_directory>")
        sys.exit(1)
    
    base_directory = sys.argv[1]
    if not os.path.isdir(base_directory):
        print(f"The directory {base_directory} does not exist.")
        sys.exit(1)
    
    stopper = DockerComposeStopper(base_directory)
    docker_compose_files = stopper.run_docker_compose_stop()
    
    if docker_compose_files:
        print("Docker Compose files found and stopped in the following directories:")
        for compose_file in docker_compose_files:
            print(os.path.dirname(compose_file))
    else:
        print("No Docker Compose files were found or stopped.")
