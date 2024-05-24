import os
from dotenv import dotenv_values

class DockerManager:
    def __init__(self, env_file=".env_docker"):
        self.env_vars = dotenv_values(env_file)

    def login(self, registry, username=None, password=None):
        """
        Log in to a Docker registry.
        """
        login_command = f"docker login {registry}"
        if username and password:
            login_command += f" -u {username} -p {password}"
        result = os.system(login_command)
        if result != 0:
            print(f"Error logging into Docker registry: {registry}")
            exit(1)
        print(f"Logged into Docker registry: {registry}")

    def build_image(self, image_name, tag="latest"):
        """
        Build a Docker image.
        """
        full_image_name = f"{image_name}:{tag}"
        build_command = f"docker build -t {full_image_name} ."
        result = os.system(build_command)
        if result != 0:
            print(f"Error building Docker image: {full_image_name}")
            exit(1)
        print(f"Docker image built: {full_image_name}")
        return full_image_name

    def push_image(self, image_name):
        """
        Push a Docker image to a registry.
        """
        push_command = f"docker push {image_name}"
        result = os.system(push_command)
        if result != 0:
            print(f"Error pushing Docker image: {image_name}")
            exit(1)
        print(f"Docker image pushed: {image_name}")

    def build_and_push(self):
        """
        Build and push Docker images to registries specified in the .env file.
        """
        image_name = self.env_vars.get("DOCKER_IMAGE_NAME")
        tag = self.env_vars.get("DOCKER_TAG", "latest")
        
        registries = [key for key in self.env_vars.keys() if key.endswith('_NAME')]

        for registry_key in registries:
            registry = self.env_vars[registry_key]
            full_image_name = f"{registry}/{image_name}:{tag}"
            
            self.build_image(image_name, tag)
            self.login(registry, self.env_vars.get("DOCKER_USERNAME"), self.env_vars.get("DOCKER_PASSWORD"))
            self.push_image(full_image_name)

if __name__ == "__main__":
    docker_manager = DockerManager()
    docker_manager.build_and_push()
