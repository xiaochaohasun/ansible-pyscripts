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
        git_down_path = gits_path + g.split("/")[-1]
        if os.path.exists(git_down_path):
            cd_cmd = "cd %s" % git_down_path
            subprocess.call(cd_cmd, shell=True)
            git_cmd = "git pull"
        else:
            git_cmd = "git clone %s %s" % (g, git_down_path)
        subprocess.call(git_cmd, shell=True)

if __name__ == '__main__':
    main()


#ansible不支持讲git文件下载到本地，只能下载到远程主机，使用此脚本提前执行下载到指定路径，直接使用ansible，copy模块即可。
#将要下载的文件列别放入g_list即可。