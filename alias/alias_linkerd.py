#linkerd
def linkerd(alias_manager):
    print("______________LINKERD")
    alias_manager.add_alias('l_check_east', 'linkerd check --pre --context east')
    alias_manager.add_alias('l_check_west', 'linkerd check --pre --context west')
    alias_manager.add_alias('l_clan_multi_clusters', 'cd /home/multicloud/ && ./clean_cluster.sh ')
    alias_manager.add_alias('l_check_gateway_multicluster', 'echo "Verificando los gateways..." && linkerd multicluster --context east gateways && linkerd multicluster --context west gateways')