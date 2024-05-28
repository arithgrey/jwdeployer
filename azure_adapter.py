import os
import yaml

class AzurePipelineModifier:
    def __init__(self, filename):
        self.filename = filename

    def read_yaml(self):
        with open(self.filename, 'r') as file:
            data = yaml.safe_load(file)
        return data

    def modify_yaml(self, new_data):
        with open(self.filename, 'w') as file:
            yaml.dump(new_data, file)

    def add_variable(self, name, value):
        data = self.read_yaml()
        if 'variables' not in data:
            data['variables'] = {}
        data['variables'][name] = value
        self.modify_yaml(data)

if __name__ == "__main__":
    filename = os.path.join(".ci", "pipe", "azure-pipelines_beta.yaml")
    modifier = AzurePipelineModifier(filename)

    # Define nuevas variables
    variables_to_add = {
        "ACR": "ACR-TYSON-BETA-V2",
        "referenciaACR": ".azurecr.io",
        "AzureProjectName": "findep-calidad-uat-mx"
    }

    # Agregar nuevas variables al archivo YAML
    for name, value in variables_to_add.items():
        modifier.add_variable(name, value)
