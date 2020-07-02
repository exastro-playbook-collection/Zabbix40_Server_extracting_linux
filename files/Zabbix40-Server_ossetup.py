import re
import json
import sys
import os

# main process
args = sys.argv

if (len(args) < 2):
    sys.exit(1)

path = args[1]
if(path[-1:] == "/"):
    path = path[:-1]
start_mysqld_path = path + '/command/7/stdout.txt'
start_httpd_path = path + '/command/8/stdout.txt'
start_zabbixserver_path = path + '/command/9/stdout.txt'
chkconfig_mysqld = path + '/command/10/stdout.txt'
chkconfig_httpd = path + '/command/11/stdout.txt'
chkconfig_zabbixserver = path + '/command/12/stdout.txt'
result = {}
if os.path.isfile(start_mysqld_path):
    fo = open(start_mysqld_path)
    alllines = fo.readlines()
    for strline in alllines:
        str_match = re.match('\s*Active\s*:\s*active.*running.*', strline)
        if str_match is not None:
            result['VAR_Zabbix40SV_start_mysqld'] = 'start'
            break
    fo.close()
if os.path.isfile(start_httpd_path):
    fo = open(start_httpd_path)
    alllines = fo.readlines()
    for strline in alllines:
        str_match = re.match('\s*Active\s*:\s*active\s*(running).*', strline)
        if str_match is not None:
            result['VAR_Zabbix40SV_start_httpd'] = 'start'
            break
    fo.close()
if os.path.isfile(start_zabbixserver_path):
    fo = open(start_zabbixserver_path)
    alllines = fo.readlines()
    for strline in alllines:
        str_match = re.match('\s*Active\s*:\s*active\s*(running).*', strline)
        if str_match is not None:
            result['VAR_Zabbix40SV_start_zabbixserver'] = 'start'
            break
    fo.close()
if os.path.isfile(chkconfig_mysqld):
    fo = open(chkconfig_mysqld)
    alllines = fo.readlines()
    for strline in alllines:
        str_match = re.match('\s*mariadb.service\s+disabled\s*', strline)
        if str_match is not None:
            result['VAR_Zabbix40SV_chkconfig_mysqld'] = False
            break
        str_match = re.match('\s*mariadb.service\s+enabled\s*', strline)
        if str_match is not None:
            result['VAR_Zabbix40SV_chkconfig_mysqld'] = True
            break
    fo.close()
if os.path.isfile(chkconfig_httpd):
    fo = open(chkconfig_httpd)
    alllines = fo.readlines()
    for strline in alllines:
        str_match = re.match('\s*httpd.service\s+disabled\s*', strline)
        if str_match is not None:
            result['VAR_Zabbix40SV_chkconfig_httpd'] = False
            break
        str_match = re.match('\s*httpd.service\s+enabled\s*', strline)
        if str_match is not None:
            result['VAR_Zabbix40SV_chkconfig_httpd'] = True
            break
    fo.close()
if os.path.isfile(chkconfig_zabbixserver):
    fo = open(chkconfig_zabbixserver)
    alllines = fo.readlines()
    for strline in alllines:
        str_match = re.match('zabbix-server.service\s+disabled\s*', strline)
        if str_match is not None:
            result['VAR_Zabbix40SV_chkconfig_zabbixserver'] = False
            break
        str_match = re.match('zabbix-server.service\s+enabled\s*', strline)
        if str_match is not None:
            result['VAR_Zabbix40SV_chkconfig_zabbixserver'] = True
            break
    fo.close()

print(json.dumps(result))
