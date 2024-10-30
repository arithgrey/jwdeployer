#git
def git(alias_manager):
    print("______________GIT")
    alias_manager.add_alias("g_chore_devops",'git add . && git commit -m "[FEAT] devops tools" && git push')
    alias_manager.add_alias("g_stash","git stash")
    alias_manager.add_alias("g_stash_apply","git stash apply")
    alias_manager.add_alias("g_st","git status")
    alias_manager.add_alias("g_co_b","git checkout")
    alias_manager.add_alias("g_co","git checkout ")
    alias_manager.add_alias("g_br","git branch")
    alias_manager.add_alias("g_pull","git pull")
    alias_manager.add_alias("g_merge","git merge ")
    
    