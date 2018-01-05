#!/usr/bin/env python
# -*- coding:utf8 -*-

import os
import subprocess
import sys


gits_path = "/data/ansible_scripts/ansible_script/ansible_gits/" #download path
git_cmd = ""


def get_git_list(gits_file):
    fobj = open(gits_file)
    gits = fobj.readlines()
    git_list = []
    for _git in gits:
        if _git != "\n":
            git_list.append(_git)
    fobj.close()
    return git_list


def main(gits_file):
    git_list=get_git_list(gits_file)
    for g in git_list:
        git_down_path = gits_path + g.split(":")[-1].split("/")[-1].split(".git")[0]
        if os.path.exists(git_down_path):
            os.chdir(git_down_path)
            out_str = "cd %s && git pull" % git_down_path
            print out_str
            git_cmd = "git pull"
        else:
            os.chdir(gits_path)
            git_cmd = "git clone %s" % (g)
            out_str = "cd %s && %s" % (gits_path, g)
            print out_str
        subprocess.call(git_cmd, shell=True)


if __name__ == '__main__':
    if len(sys.argv) >= 1:
        gits_file=sys.argv[1]
        main(gits_file)


# ansible不支持讲git文件下载到本地，只能下载到远程主机，使用此脚本提前执行下载到指定路径，直接使用ansible，copy模块即可。
# 将要下载的gitd地址放入gits_file文件中即可。
