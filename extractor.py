import yaml

class EnvConfigurator:
    def __init__(self, yaml_file, env_config_file):
        self.yaml_file = yaml_file
        self.env_config_file = env_config_file

    def read_yaml(self):
        with open(self.yaml_file, 'r') as file:
            return yaml.safe_load(file)

    def extract_variables(self, data):
        return data.get('variables', {})

    def save_env_config(self, variables):
        with open(self.env_config_file, 'w') as file:
            for key, value in variables.items():
                file.write(f"{key.upper()}={value}\n")

    def configure_environment(self):
        data = self.read_yaml()
        variables = self.extract_variables(data)
        self.save_env_config(variables)
        
        with open(self.env_config_file, 'a') as file:
            file.write("# Configuraciones de Docker\n")
            file.write("# GCR_NAME=gcr.io/my-gcp-project\n")
            file.write("# ECR_NAME=aws_account_id.dkr.ecr.region.amazonaws.com/my-ecr-repo\n")
            file.write("# DOCKER_IMAGE_NAME=fastapi-service\n")
            file.write("# DOCKER_TAG=1.1\n")
