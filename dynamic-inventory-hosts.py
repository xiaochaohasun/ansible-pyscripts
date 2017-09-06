#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
import sys
import json
import urllib2
import simplejson

#api-ip-port
JUMPSERVER_IP_PORT = "http://ip:port"
GROUP_URL = JUMPSERVER_IP_PORT + "/api/listgroup/"
HOSTS_URL = JUMPSERVER_IP_PORT + "/api/listasset/?groupid="


def groups():
    g_list_url = urllib2.Request(GROUP_URL)
    response = urllib2.urlopen(g_list_url)
    g_list = response.read()
    return simplejson.loads(g_list)

def allHosts():
    all_groups = groups()
    h_list_r = {}
    for (gid, gname) in all_groups.items():
        h = []
        h_url = HOSTS_URL + "%s" % gid
        h_list_url = urllib2.Request(h_url)
        response = urllib2.urlopen(h_list_url)
        h_list = response.read()
        h_2_dict = simplejson.loads(h_list)
        for (k, v) in h_2_dict.items():
            h.append(v['ip'])
        hosts = {"hosts": h}
        h_list_r[gname] = hosts
    return json.dumps(h_list_r, indent=4)


def hosts(name):
    r = {'ansible_ssh_port': '22'}
    cpis = dict(r.items())
    return json.dumps(cpis, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--list', help='host list', action='store_true')
    parser.add_argument('-H', '--host', help='host vars')
    args = vars(parser.parse_args())

    if args['list']:
        print allHosts()
    elif args['host']:
        print hosts(args['host'])
    else:
        parser.print_help()



#根据官方要求，必须返回固定格式的json字符串，脚本还必须支持--list参数。

#方法处理前从api获取回来的数据格式如下，可以根据自己api返回的数据做调整，最好是json格式。

#groups-api获取到的数据格式
#｛"1":"tmp","2","web"｝

#单个组(根据组id)返回的数据格式如下
{"1": {"ip": "192.168.1.2", "hostname": "tmp1"},"2": {"ip": "192.168.1.3", "hostname": "tmp2"}}


#方法处理后返回数据

#方法 groups 返回
#｛"1":"tmp","2","web"｝

#方法：allHosts 返回
#python hosts.py --list
# {
#     "tmp": {
#         "hosts": [
#             "192.168.1.2",
#             "192.168.1.3"
#         ]
#     },
#     "web": {
#         "hosts": [
#             "10.10.2.5",
#         ]
#     }
# }

#方法 hosts 返回
#python hosts.py -H 192.168.1.2
#｛"ansible_ssh_port":"22"｝