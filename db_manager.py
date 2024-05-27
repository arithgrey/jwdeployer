import os

class ConfigReader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.configuration = {}

    def read_configuration(self):
        with open(self.file_name) as file:
            for line in file:
                if line.strip() and not line.strip().startswith('#'):
                    key, value = line.strip().split('=', 1)
                    self.configuration[key] = value

    def get_configuration(self):
        return self.configuration

class HelmCommandGenerator:
    def __init__(self, configuration):
        self.configuration = configuration

    def generate_helm_command(self):
        db_type = self.configuration.get('DBTYPE')
        db_instance = self.configuration.get('DBINSTANCE')
        db_user = self.configuration.get('DBUSER')
        db_password = self.configuration.get('DBPASSWORD')
        
        if db_type and db_instance:
            helm_command = f'helm install {db_instance} bitnami/{db_type}'
            # Añadir las credenciales de usuario y contraseña como flags al comando Helm
            helm_command += f' --set postgresql.postgresUser={db_user}'
            helm_command += f' --set postgresql.postgresPassword={db_password}'
            return helm_command
        else:
            return None

def main():
    config_file = '.env_conf'
    if os.path.exists(config_file):
        config_reader = ConfigReader(config_file)
        config_reader.read_configuration()
        configuration = config_reader.get_configuration()

        helm_command_generator = HelmCommandGenerator(configuration)
        helm_command = helm_command_generator.generate_helm_command()

        if helm_command:
            print("Comando Helm generado:")
            print(helm_command)
        else:
            print("No se encontraron las variables de entorno necesarias en el archivo de configuración.")
    else:
        print("El archivo de configuración .env_conf no existe.")

if __name__ == "__main__":
    main()
