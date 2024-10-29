#pip
def docker(alias_manager):
    print("______________DOCKER")
    alias_manager.add_alias('d_up_build','docker-compose up --build')
    alias_manager.add_alias('d_down_v', 'go_jw_service && act_env && python docker_down.py /home/arithgrey/enid_service/services/')