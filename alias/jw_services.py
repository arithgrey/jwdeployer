#jw service
def jw(alias_manager):
    print("______________Jw services")
    alias_manager.add_alias('jw_checker', 'go_jw_service && activate_env &&  python git_status_checker.py /home/arithgrey/enid_service/services')