#!/bin/env python

import sys
import subprocess


USER='guofubao'
PASSWD='WeeF*K&N'

def usage():
    fname='%s' % sys.argv[0]
    print '''\033[32;1mexample:\033[0m
\033[32;1m%s hosts.txt\033[0m
\033[31;1mhosts.txt\033[0m is file,has multiple host ip or hostname.''' % fname




def get_hosts(filename):
    fobj = open(filename)
    host_list=fobj.readlines()
    fobj.close()
    return host_list


def ssh_publicKey(host_list):
    for host in host_list:
	if host != '\n':
            print '\033[31;1mNow,ssh-copy-id to : %s\033[0m' % (host)
            ssh_cmd='sshpass -p "%s" ssh-copy-id -o StrictHostKeyChecking=no %s@%s' % (PASSWD,USER,host)
            subprocess.call(ssh_cmd,shell=True)
        

def main():
    filename = sys.argv[1]
    host_list=get_hosts(filename)
    ssh_publicKey(host_list)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        usage()
        sys.exit()
    if sys.argv[1] == '-h':
        usage()
        sys.exit()
    main()
