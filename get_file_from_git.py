#!/usr/bin/env python
# -*- coding:utf8 -*-

import os
import subprocess

git_list = ["git@git.xxx.com:system_conf/sudoers.git", "git@git.xxx.com:system_conf/iptables.git",
            "git@git.xxx.com:system_conf/vim.git", "git@git.xxx.com:system_conf/hosts.git"]

gits_path = "/tmp/ansible_gits/"
git_cmd = ""

def main():
    for g in git_list:
        git_down_path = gits_path + g.split(":")[-1].split("/")[-1].split(".git")[0]
        if os.path.exists(git_down_path):
	    os.chdir(git_down_path)
	    out_str="cd %s && git pull" % git_down_path
            print out_str
            git_cmd = "git pull"
        else:
	    os.chdir(gits_path)
	    git_cmd = "git clone %s" % (g)
	    out_str="cd %s && %s" % (gits_path,g)
	    print out_str
        subprocess.call(git_cmd, shell=True)


if __name__ == '__main__':
    main()


#ansible不支持讲git文件下载到本地，只能下载到远程主机，使用此脚本提前执行下载到指定路径，直接使用ansible，copy模块即可。
#将要下载的文件列别放入g_list即可。
