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
localpkg_dst_path = path + '/command/5/stdout.txt'
localpkg_src_path = path + '/command/6/stdout.txt'
result = {}

if os.path.isfile(localpkg_dst_path):
    fo = open(localpkg_dst_path)
    alllines = fo.readlines()
    for strline in alllines:
        str_match = re.match('\s*VAR_Zabbix40SV_localpkg_dst\s+(.*)', strline)
        if str_match is not None:
            result['VAR_Zabbix40SV_localpkg_dst'] = str_match.group(1).strip()
            break
    fo.close()
if os.path.isfile(localpkg_src_path):
    fo = open(localpkg_src_path)
    alllines = fo.readlines()
    for strline in alllines:
        str_match = re.match('\s*VAR_Zabbix40SV_localpkg_src\s+(.*)', strline)
        if str_match is not None:
            result['VAR_Zabbix40SV_localpkg_src'] = str_match.group(1).strip()
            break
    fo.close()
result['VAR_Zabbix40SV_phpbcmath_src'] = 'php-bcmath-5.4.16-46.el7.x86_64.rpm'
result['VAR_Zabbix40SV_phpmbstring_src'] = 'php-mbstring-5.4.16-46.el7.x86_64.rpm'
result['VAR_Zabbix40SV_trousers_src'] = 'trousers-0.3.14-2.el7.i686.rpm'
print(json.dumps(result))
