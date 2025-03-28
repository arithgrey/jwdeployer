#general
def commons(alias_manager):
    # Agregar alias
    print("______________COMMONS")
    alias_manager.add_alias('access_token_cluster', 'kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep rancher | awk "{print $1}")')
    alias_manager.add_alias('activate_env', 'source env/bin/activate')
    alias_manager.add_alias('add_alias', 'nano  ~/.bashrc')
    alias_manager.add_alias('add_env', 'python3 -m venv env && source env/bin/activate')
    alias_manager.add_alias('add_env_3.10', 'python3.10 -m venv env && source env/bin/activate')
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
    alias_manager.add_alias('pull_main', 'git checkout main && git pull origin main')

    alias_manager.add_alias('reset_nginx', 'sudo systemctl restart nginx && systemctl status nginx && nginx -t')
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
    alias_manager.add_alias('d_down', 'docker-compose down')
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

    #Kubernetes
    alias_manager.add_alias('g_clusters', 'minikube profile list')
    alias_manager.add_alias('g_nodes', 'kubectl get nodes')
    alias_manager.add_alias('grep', 'grep --color=auto')
    alias_manager.add_alias('install_istio_', 'istioctl install --set profile=demo -y')
    alias_manager.add_alias('install_istio_on_cluster_1', 'istioctl install --context="${CTX_CLUSTER1}" -f cluster1.yaml -y')
    alias_manager.add_alias('install_istio_on_cluster_2', 'istioctl install --context="${CTX_CLUSTER2}" -f cluster2.yaml -y')
    alias_manager.add_alias('ip_mini', 'minikube ip')
    alias_manager.add_alias('k_apply_', 'kubectl apply -f .')
    alias_manager.add_alias('k_use_context_', 'kubectl config use-context ')
    alias_manager.add_alias('k_show_context_', 'kubectl config get-contexts')
    alias_manager.add_alias('k_get_ingress_ip', 'kubectl get svc istio-ingressgateway -n istio-system')

    alias_manager.add_alias('go_ngx', 'cd /home/arithgrey/enid_service/services/service_web')
    alias_manager.add_alias('k_gateways', 'kubectl get gateways -A')
    #heml 

    alias_manager.add_alias('l_helm', 'helm list')
    alias_manager.add_alias('delete_heml', 'helm delete')


    #k8s
    alias_manager.add_alias('m_start', 'minikube start --force')
    alias_manager.add_alias('m_stop', 'minikube stop --force')
    alias_manager.add_alias('cln_minikube', 'minikube delete --all')
    alias_manager.add_alias('delete_cluster_by_name', 'minikube delete -p ')


    #pip
    alias_manager.add_alias('pip_fr', 'pip freeze > requirements.txt')
    alias_manager.add_alias('pip_inst_requirements', 'pip install -r requirements.txt')
    alias_manager.add_alias('deact', 'deactivate')
    alias_manager.add_alias('pip_ls', 'pip list')
    alias_manager.add_alias('act_env', 'source env/bin/activate')


    #service
    alias_manager.add_alias('jw_srv', 'git clone git@github.com:arithgrey/jwdeployer.git && cd jwdeployer && python3 -m venv env && source env/bin/activate && pip install -r requirements.txt && python alias_manager.py')
    alias_manager.add_alias('jw_service', 'jw_srv && python alias_manager.py')
    alias_manager.add_alias('jw_deployment', 'python deployment_to_kubernets.py')
    alias_manager.add_alias('jw_db', 'python db_manager.py')
    alias_manager.add_alias('jw_adapter', 'python azure_adapter.py')
    alias_manager.add_alias('jw_git_manager', 'python gitignore_manager.py')
    alias_manager.add_alias('jw_docker_manager','python dockerignore_manager.py')
    alias_manager.add_alias('jw_clean_service','cd .. && rm -Rf jwdeployer')
    alias_manager.add_alias('jw_clone_service','python repository_manager.py')
    alias_manager.add_alias('jw_alias_service','python alias_manager.py')
    alias_manager.add_alias('jw_repository_service','go_jw_service && activate_env && python repository_manager.py')
    alias_manager.add_alias('jw_docker_compose_runner_service','python docker_compose_runner.py')
    alias_manager.add_alias('jw_docker_compose_runner','python compose_runner.py')
    alias_manager.add_alias('jw_pull_service', 'go_jw_service &&  activate_env && python pull_manager.py')
    alias_manager.add_alias('_jw_pull_service', '_go_jw_service &&  activate_env && python _pull_manager.py')

    #alias
    alias_manager.add_alias('update_alias', 'source  ~/.bashrc')

    #docker
    alias_manager.add_alias('d_inspect_img', 'docker image inspect ')

    #java 

    alias_manager.add_alias('mvn_run', 'mvn spring-boot:run')

    #git

    alias_manager.add_alias('g_cb', 'git checkout -b')
    alias_manager.add_alias('g_add_', 'git add .')
    alias_manager.add_alias('g_comm_', 'git commit -m ')
    alias_manager.add_alias('g_push', 'git push')
    alias_manager.add_alias('g_mixed', 'git reset --mixed ')
    alias_manager.add_alias('g_st', 'git status')

    alias_manager.add_alias('local_status', 'go_jw_service && activate_env && python git_status_checker.py /home/arithgrey/enid_service/services')
    alias_manager.add_alias('enid_status', '_go_jw_service &&  activate_env && python git_status_checker.py /home/_enid_service/services')


    #DOCS
    alias_manager.add_alias('show_readme', 'add_env && pip install grip && grip')
    # Agregar nuevos alias para kubectl e istioctl
    alias_manager.add_alias('k_kubectl', 'kubectl')
    alias_manager.add_alias('k_get_pods', 'kubectl get pods')
    alias_manager.add_alias('k_get_deployments', 'kubectl get deployments')
    alias_manager.add_alias('k_get_services', 'kubectl get services')
    alias_manager.add_alias('k_get_namespaces', 'kubectl get namespaces')
    alias_manager.add_alias('k_get_clusters', 'kubectl get clusters')
    alias_manager.add_alias('k_get_secrets', 'kubectl get secrets')
    alias_manager.add_alias('k_get_configmaps', 'kubectl get configmaps')
    alias_manager.add_alias('k_describe_pod', 'kubectl describe pod')
    alias_manager.add_alias('k_describe_deployment', 'kubectl describe deployment')
    alias_manager.add_alias('k_describe_service', 'kubectl describe service')
    alias_manager.add_alias('k_describe_namespace', 'kubectl describe namespace')
    alias_manager.add_alias('k_apply_file', 'kubectl apply -f')
    alias_manager.add_alias('k_delete_file', 'kubectl delete -f')
    alias_manager.add_alias('k_logs', 'kubectl logs')
    alias_manager.add_alias('k_exec_into_pod', 'kubectl exec -it')

    alias_manager.add_alias('k_delete', 'kubectl delete -f .')
    alias_manager.add_alias('k_search_pod', 'k_get_pods -A  | grep ')

    # Alias de istioctl
    alias_manager.add_alias('k_istio_version', 'istioctl version')
    alias_manager.add_alias('k_istio_proxy_status', 'istioctl proxy-status')
    alias_manager.add_alias('k_istio_authz', 'istioctl authz check')
    alias_manager.add_alias('k_istio_metrics', 'istioctl metrics')
    alias_manager.add_alias('k_istio_describe', 'istioctl describe')
    alias_manager.add_alias('k_istio_get_virtual_services', 'istioctl get virtualservices')
    alias_manager.add_alias('k_istio_get_destinations', 'istioctl get destinationrules')
    alias_manager.add_alias('k_istio_config_dump', 'istioctl proxy-config dump')
    alias_manager.add_alias('k_istio_addons', 'istioctl manifest apply --set values.grafana.enabled=true --set values.prometheus.enabled=true --set values.kiali.enabled=true')
    alias_manager.add_alias('k_istio_apply', 'istioctl apply -f')
    alias_manager.add_alias('k_istio_delete', 'istioctl delete -f')
    alias_manager.add_alias('k_istio_check_inject', 'istioctl check-inject')
    alias_manager.add_alias('k_istio_inject', 'istioctl kube-inject -f')
    alias_manager.add_alias('k_istio_wait', 'istioctl wait --for=condition=ready')
    alias_manager.add_alias('k_exec', 'kubectl exec -it')


    alias_manager.add_alias('k_get_all_resources', 'kubectl get all --all-namespaces')
    alias_manager.add_alias('k_scale_deployment', 'kubectl scale --replicas=')
    alias_manager.add_alias('k_create_namespace', 'kubectl create namespace')
    alias_manager.add_alias('k_delete_namespace', 'kubectl delete namespace')
    alias_manager.add_alias('k_get_persistent_volumes', 'kubectl get pv')
    alias_manager.add_alias('k_get_persistent_volume_claims', 'kubectl get pvc')
    alias_manager.add_alias('k_get_events_sorted', 'kubectl get events --sort-by=.metadata.creationTimestamp')
    alias_manager.add_alias('k_describe_replica_set', 'kubectl describe rs')
    alias_manager.add_alias('k_get_replica_sets', 'kubectl get rs')
    alias_manager.add_alias('k_get_jobs', 'kubectl get jobs')
    alias_manager.add_alias('k_describe_job', 'kubectl describe job')
    alias_manager.add_alias('k_get_cron_jobs', 'kubectl get cronjobs')
    alias_manager.add_alias('k_describe_cron_job', 'kubectl describe cronjob')
    alias_manager.add_alias('k_get_endpoints', 'kubectl get endpoints')
    alias_manager.add_alias('k_describe_endpoints', 'kubectl describe endpoints')
    alias_manager.add_alias('k_apply_resources', 'kubectl apply -k')
    alias_manager.add_alias('k_edit_deployment', 'kubectl edit deployment')
    alias_manager.add_alias('k_rollout_history', 'kubectl rollout history deployment')
    alias_manager.add_alias('k_rollout_undo', 'kubectl rollout undo deployment')
    alias_manager.add_alias('k_get_storage_classes', 'kubectl get storageclass')
    alias_manager.add_alias('k_describe_storage_class', 'kubectl describe storageclass')
    alias_manager.add_alias('k_get_ingresses', 'kubectl get ingresses')
    alias_manager.add_alias('k_describe_ingress', 'kubectl describe ingress')
    alias_manager.add_alias('k_get_network_policies', 'kubectl get networkpolicies')
    alias_manager.add_alias('k_describe_network_policy', 'kubectl describe networkpolicy')
    alias_manager.add_alias('k_get_service_accounts', 'kubectl get sa')
    alias_manager.add_alias('k_describe_service_account', 'kubectl describe sa')
    alias_manager.add_alias('k_get_failed_pods', 'kubectl get pods --field-selector=status.phase=Failed')
    alias_manager.add_alias('k_get_running_pods', 'kubectl get pods --field-selector=status.phase=Running')
    alias_manager.add_alias('k_get_stopped_pods', 'kubectl get pods --field-selector=status.phase=Succeeded')
    alias_manager.add_alias('k_get_pending_pods', 'kubectl get pods --field-selector=status.phase=Pending')
    alias_manager.add_alias('k_get_terminated_pods', 'kubectl get pods --field-selector=status.phase=Failed --show-labels')
    alias_manager.add_alias('k_get_pod_logs', 'kubectl logs --previous')
    alias_manager.add_alias('k_describe_failed_pod', 'kubectl describe pod $(kubectl get pods --field-selector=status.phase=Failed -o jsonpath="{.items[0].metadata.name}")')
    alias_manager.add_alias('k_get_container_status', 'kubectl get pods -o jsonpath="{.items[*].status.containerStatuses[*].state}"')
    alias_manager.add_alias('k_get_pod_events', 'kubectl get events --field-selector involvedObject.kind=Pod')
    alias_manager.add_alias('k_get_unhealthy_pods', 'kubectl get pods --field-selector=status.phase!=Running')
    alias_manager.add_alias('k_get_deployment_events', 'kubectl get events --field-selector involvedObject.kind=Deployment')
    alias_manager.add_alias('k_get_job_status', 'kubectl get jobs --output=wide')
    alias_manager.add_alias('k_get_cronjob_status', 'kubectl get cronjobs --output=wide')
    alias_manager.add_alias('k_get_all_container_logs', 'kubectl logs --all-containers=true')
    alias_manager.add_alias('k_get_pod_resource_usage', 'kubectl top pods')
    alias_manager.add_alias('k_get_node_resource_usage', 'kubectl top nodes')
    alias_manager.add_alias('k_get_deployment_rollout_status', 'kubectl rollout status deployment')
    alias_manager.add_alias('k_get_stuck_pods', 'kubectl get pods --field-selector=status.phase!=Running')
    alias_manager.add_alias('k_get_failed_containers', 'kubectl get pods -o jsonpath="{.items[?(@.status.containerStatuses[?(@.state.waiting)])].metadata.name}"')
    alias_manager.add_alias('k_check_container_restart_count', 'kubectl get pods -o jsonpath="{.items[*].status.containerStatuses[?(@.restartCount>0)].name}"')
    alias_manager.add_alias('k_get_hpa', 'kubectl get hpa')
    alias_manager.add_alias('k_describe_hpa', 'kubectl describe hpa')
    alias_manager.add_alias('k_delete_pod', 'kubectl delete pod')
    alias_manager.add_alias('k_get_virtual_service', 'kubectl get virtualservice')
    # Alias para obtener información de recursos
    alias_manager.add_alias('k_get_top_pods', 'kubectl top pods')
    alias_manager.add_alias('k_get_top_nodes', 'kubectl top nodes')
    alias_manager.add_alias('k_get_resource_quota', 'kubectl get resourcequota')
    alias_manager.add_alias('k_describe_resource_quota', 'kubectl describe resourcequota')
    alias_manager.add_alias('k_get_pod_resource_limits', 'kubectl get pods -o=jsonpath="{.items[*].spec.containers[*].resources}"')
    alias_manager.add_alias('k_get_pod_status', 'kubectl get pods -o=custom-columns="NAME:.metadata.name,STATUS:.status.phase,RESTARTS:.status.containerStatuses[0].restartCount"')
    alias_manager.add_alias('k_get_node_info', 'kubectl describe nodes')
    alias_manager.add_alias('k_get_container_logs_with_timestamps', 'kubectl logs --timestamps')
    alias_manager.add_alias('k_get_events_for_workload', 'kubectl get events --field-selector involvedObject.kind=Deployment')
    alias_manager.add_alias('k_get_pod_conditions', 'kubectl get pods -o=jsonpath="{.items[*].status.conditions}"')
    alias_manager.add_alias('k_exec_curl', 'k_exec  curlpod -- /bin/sh')

    # Alias para identificar problemas en cargas de trabajo
    alias_manager.add_alias('k_get_failed_deployments', 'kubectl get deployments --field-selector=status.replicas!=status.availableReplicas')
    alias_manager.add_alias('k_get_overutilized_pods', 'kubectl get pods --sort-by=.status.containerStatuses[0].restartCount --field-selector=status.phase!=Running')
    alias_manager.add_alias('k_get_high_memory_usage', 'kubectl top pods --sort-by=MEMORY')
    alias_manager.add_alias('k_get_high_cpu_usage', 'kubectl top pods --sort-by=CPU')
    alias_manager.add_alias('k_get_stuck_jobs', 'kubectl get jobs --field-selector=status.succeeded=0,status.failed>0')
    alias_manager.add_alias('k_get_recently_crashed_pods', 'kubectl get pods --field-selector=status.phase=Failed --sort-by=.status.startTime')
    alias_manager.add_alias('k_get_unscheduled_pods', 'kubectl get pods --field-selector=status.phase=Pending')
    alias_manager.add_alias('k_get_pod_restart_counts', 'kubectl get pods --output=jsonpath="{.items[*].metadata.name} {.status.containerStatuses[*].restartCount}"')
    alias_manager.add_alias('k_get_pod_resource_requests', 'kubectl get pods -o=jsonpath="{.items[*].spec.containers[*].resources.requests}"')
    alias_manager.add_alias('k_get_terminated_jobs', 'kubectl get jobs --field-selector=status.succeeded>0')
    alias_manager.add_alias('k_get_service_entry', 'kubectl get serviceentry -n istio-system')
    alias_manager.add_alias('k_roll_out', 'kubectl rollout restart deployment ')

    alias_manager.add_alias('k_rollout_deployment', 'kubectl rollout restart deployment ')
    alias_manager.add_alias('k_get_current_context', 'kubectl config current-context')
    # Recargar .bashrc

    alias_manager.add_alias('enid_stop', '_go_jw_service && act_env && python service_enid_stopper.py /home/_enid_service/')
    alias_manager.add_alias('enid_up', '_go_jw_service && activate_env && jw_docker_compose_runner /home/_enid_service/services')
    alias_manager.add_alias('local_up', 'go_jw_service && activate_env && jw_docker_compose_runner_service /home/arithgrey/enid_service/services')
    alias_manager.add_alias('status_enid', 'go_scripts && make status_enid_service')
    alias_manager.add_alias('go_jw_service', 'cd /home/arithgrey/enid_service/jwdeployer')
    alias_manager.add_alias('_go_jw_service', 'cd /home/_enid_service/jwdeployer/')

    alias_manager.add_alias('_go_enid', 'cd /home/_enid_service')


    alias_manager.add_alias('go_enid_store', 'cd /home/arithgrey/enid_service/services/enid-store/enid')
    alias_manager.add_alias('go_faqs', 'cd /home/arithgrey/enid_service/services/service-faqs/')
    alias_manager.add_alias('go_frontend', 'cd /home/arithgrey/enid_service/services/service-store')
    alias_manager.add_alias('go_leads', 'cd /home/arithgrey/enid_service/services/service_leads')
    alias_manager.add_alias('go_oauth', 'cd /home/arithgrey/enid_service/services/service-oauth')
    alias_manager.add_alias('go_references', 'cd /home/arithgrey/enid_service/services/service-references')
    alias_manager.add_alias('go_reverse_proxy', 'cd /home/arithgrey/enid_service/services/reverse_proxy_nginx')
    alias_manager.add_alias('go_scripts', 'cd /home/arithgrey/enid_service/services/service-scripts-deployment')
    alias_manager.add_alias('go_stock', 'cd /home/arithgrey/enid_service/services/service_stock')
    alias_manager.add_alias('go_assintence', 'cd /home/arithgrey/enid_service/services/assintence_service/')
    alias_manager.add_alias('go_find', 'cd /home/arithgrey/findep')

    #Enid
    alias_manager.add_alias('_go_enid_store', 'cd /home/_enid_service/services/enid-store/enid')
    alias_manager.add_alias('_go_faqs', 'cd /home/_enid_service/services/service-faqs/')
    alias_manager.add_alias('_go_frontend', 'cd /home/_enid_service/services/service-store')
    alias_manager.add_alias('_go_leads', 'cd /home/_enid_service/services/service_leads')
    alias_manager.add_alias('_go_oauth', 'cd /home/_enid_service/services/service-oauth')
    alias_manager.add_alias('_go_references', 'cd /home/_enid_service/services/service-references')
    alias_manager.add_alias('_go_reverse_proxy', 'cd /home/_enid_service/services/reverse_proxy_nginx')
    alias_manager.add_alias('_go_scripts', 'cd /home/_enid_service/services/service-scripts-deployment')
    alias_manager.add_alias('_go_stock', 'cd /home/_enid_service/services/service_stock')

    
    alias_manager.add_alias('exec_leads', 'd_exec lead_service /bin/ash')
    alias_manager.add_alias('exec_enid', 'd_exec -it enid_service /bin/ash')
    alias_manager.add_alias('exec_faqs', 'd_exec -it faqs_service /bin/ash')
    alias_manager.add_alias('exec_stock', 'd_exec -it stock_service /bin/ash')
    alias_manager.add_alias('exec_oauth', 'd_exec -it oauth_service /bin/ash')
    alias_manager.add_alias('exec_assintence', 'd_exec -it assintence_ia_service /bin/ash')
    
    alias_manager.add_alias('exec_refences', 'd_exec -it references_service /bin/ash')
    alias_manager.add_alias('redis_flush','for container in $(docker ps --filter "name=redis" --format "{{.Names}}"); do docker exec -it $container redis-cli FLUSHDB; done')
    alias_manager.add_alias('local_stop','go_jw_service && act_env && python docker_stop.py /home/arithgrey/enid_service/services/')
