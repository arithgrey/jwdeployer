import os

class AliasManager:
    def __init__(self, bashrc_path=os.path.expanduser("~/.bashrc")):
        self.bashrc_path = bashrc_path

    def alias_exists(self, name):
        """Check if an alias already exists in the .bashrc file and return its line number."""
        with open(self.bashrc_path, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if line.startswith(f"alias {name}="):
                    return i
        return None

    def add_alias(self, name, command):
        alias_command = f"alias {name}='{command}'\n"
        alias_line = self.alias_exists(name)

        if alias_line is not None:
            # Update the existing alias
            with open(self.bashrc_path, 'r') as file:
                lines = file.readlines()
            lines[alias_line] = alias_command
            with open(self.bashrc_path, 'w') as file:
                file.writelines(lines)
            print(f"Alias '{name}' actualizado con éxito.")
        else:
            # Add new alias
            with open(self.bashrc_path, 'a') as file:
                file.write(alias_command)
            print(f"Alias '{name}' añadido con éxito.")

    def reload_bashrc(self):
        """Reload the .bashrc file to apply changes."""
        os.system('exec bash')
        print("Archivo .bashrc recargado.")
        
# Crear una instancia de AliasManager
alias_manager = AliasManager()

# Agregar alias
alias_manager.add_alias('access_token_cluster', 'kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep rancher | awk "{print $1}")')
alias_manager.add_alias('activate_env', 'source env/bin/activate')
alias_manager.add_alias('add_alias', 'nano  ~/.bashrc')
alias_manager.add_alias('add_env', 'python3 -m venv env && source env/bin/activate')
alias_manager.add_alias('add_namespace', 'kubectl create namespace ')
alias_manager.add_alias('alias_grep', 'alias | grep ')
alias_manager.add_alias('all_in_namespace', 'kubectl get all -n ')
alias_manager.add_alias('br', 'git branch')
alias_manager.add_alias('check_gateway_external_ip_cluster_1', 'kubectl --context="${CTX_CLUSTER1}" get svc istio-eastwestgateway -n istio-system')
alias_manager.add_alias('checkout_b', 'git checkout -b ')
alias_manager.add_alias('cln_containers', 'docker container prune -f')
alias_manager.add_alias('cln_images_docker', 'docker image prune -a')
alias_manager.add_alias('cln_minikube', 'minikube delete --all && rm -Rf istio-1.21.2/')
alias_manager.add_alias('cluster_1', 'kubectl --context findep-calidad-uat-mx get all -n test')
alias_manager.add_alias('cluster_2', 'kubectl --context findep-calidad-uat-mx-2 get all -n test')
alias_manager.add_alias('cluster_inf', 'kubectl cluster-info')
alias_manager.add_alias('co', 'git checkout')
alias_manager.add_alias('commit', 'git commit')
alias_manager.add_alias('conf_minikube', 'minikube config view')
alias_manager.add_alias('create_gateway_cluster_1', './gen-eastwest-gateway.sh  --network network1 | istioctl --context="${CTX_CLUSTER1}" install -y -f -')
alias_manager.add_alias('create_gateway_cluster_2', './gen-eastwest-gateway.sh  --network network2 | istioctl --context="${CTX_CLUSTER2}" install -y -f -')
alias_manager.add_alias('d_exec', 'docker exec -it')
alias_manager.add_alias('d_images', 'docker images')
alias_manager.add_alias('d_minikube', 'minikube delete')
alias_manager.add_alias('d_ps', 'docker ps')
alias_manager.add_alias('d_stop', 'docker stop $(docker ps -q)')
alias_manager.add_alias('d_up', 'docker-compose up')
alias_manager.add_alias('delete_cluster_1', 'minikube delete -p findep-calidad-uat-mx')
alias_manager.add_alias('delete_cluster_2', 'minikube delete -p findep-calidad-uat-mx-2')
alias_manager.add_alias('delete_cluster_by_name', 'minikube delete -p ')
alias_manager.add_alias('delete_heml', 'helm delete')
alias_manager.add_alias('deploy_airflow', 'helm install airflow apache-airflow/airflow --namespace airflow --set airflow.redis.enabled=true --set airflow.redis.usePassword=false')
alias_manager.add_alias('df', 'git diff')
alias_manager.add_alias('docker_stop', 'docker stop $(docker ps -q)')
alias_manager.add_alias('edit_nginx', 'sudo nano /etc/nginx/sites-available/proxy.conf')
alias_manager.add_alias('egrep', 'egrep --color=auto')
alias_manager.add_alias('export_cluster_names', 'export CTX_CLUSTER1=cluster1 && export CTX_CLUSTER1=cluster2')
alias_manager.add_alias('expose_1', 'minikube service hola-mundo --profile="findep-calidad-uat-mx" -n test --url')
alias_manager.add_alias('expose_2', 'minikube service hola-mundo --profile="findep-calidad-uat-mx-2" -n test --url')
alias_manager.add_alias('expose_fastapi', 'kubectl port-forward svc/fastapi-service-v1-stable 8080:80 -n devops')
alias_manager.add_alias('expose_services_on_cluster_1', 'kubectl --context="${CTX_CLUSTER1}" apply -n istio-system -f expose-services.yaml')
alias_manager.add_alias('fgrep', 'fgrep --color=auto')
alias_manager.add_alias('g_clusters', 'minikube profile list')
alias_manager.add_alias('g_nodes', 'kubectl get nodes')
alias_manager.add_alias('grep', 'grep --color=auto')
alias_manager.add_alias('install_istio_', 'istioctl install --set profile=demo -y')
alias_manager.add_alias('install_istio_on_cluster_1', 'istioctl install --context="${CTX_CLUSTER1}" -f cluster1.yaml -y')
alias_manager.add_alias('install_istio_on_cluster_2', 'istioctl install --context="${CTX_CLUSTER2}" -f cluster2.yaml -y')
alias_manager.add_alias('ip_mini', 'minikube ip')
alias_manager.add_alias('k_apply_', 'kubectl apply -f .')

#heml 

alias_manager.add_alias('l_helm', 'helm list')
alias_manager.add_alias('delete_heml', 'helm delete')


#k8s
alias_manager.add_alias('m_start', 'minikube start --force')
alias_manager.add_alias('cln_minikube', 'minikube delete --all')
alias_manager.add_alias('delete_cluster_by_name', 'minikube delete -p ')


#pip
alias_manager.add_alias('pip_fr', 'pip freeze > requirements.txt')
alias_manager.add_alias('pip_inst_requirements', 'pip install -r requirements.txt')
alias_manager.add_alias('deact', 'deactivate')



#service
alias_manager.add_alias('jw_srv', 'git clone git@github.com:arithgrey/jwdeployer.git && cd jwdeployer && python3 -m venv env && source env/bin/activate && pip install -r requirements.txt && python alias_manager.py')
alias_manager.add_alias('jw_service', 'jw_srv && python alias_manager.py')
alias_manager.add_alias('jw_deployment', 'python deployment_to_kubernets.py')
alias_manager.add_alias('jw_db', 'python db_manager.py')
alias_manager.add_alias('jw_adapter', 'python azure_adapter.py')
alias_manager.add_alias('jw_git_manager', 'python gitignore_manager.py')
alias_manager.add_alias('jw_docker_manager','python dockerignore_manager.py')

#alias
alias_manager.add_alias('update_alias', 'source  ~/.bashrc')

#docker
alias_manager.add_alias('d_inspect_img', 'docker image inspect ')

#java 

alias_manager.add_alias('mvn_run', 'mvn spring-boot:run')

# Recargar .bashrc
alias_manager.reload_bashrc()
