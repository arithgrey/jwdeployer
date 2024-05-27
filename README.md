# Add alias to local use

alias jw_service='git clone git@github.com:arithgrey/jwdeployer.git && cd jwdeployer && python3 -m venv env && source env/bin/activate && pip install -r  requirements.py'

alias jw_deployment='python deployment_to_kubernets.py'


#  postgrest 
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm install local-postgresql bitnami/postgresql


# Mongo
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm install my-mongodb bitnami/mongodb
