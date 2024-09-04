#linkerd
def linkerd(alias_manager):
    print("______________LINKERD")
    alias_manager.add_alias('check_east', 'linkerd check --pre --context east')
    alias_manager.add_alias('check_west', 'linkerd check --pre --context west')
    alias_manager.add_alias('clan_multi_clusters', 'cd /home/multicloud/ && ./clean_cluster.sh ')
