# -*- coding: UTF-8 -*-
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
myconf_path = path + '/command/0/stdout.txt'
zabbixServerConf_path = path + '/command/1/stdout.txt'
zabbixConfPhp_path = path + '/command/2/stdout.txt'
zabbixConf_path = path + '/command/3/stdout.txt'
zabbixServer_path = path + '/command/4/stdout.txt'
result = {}

# For my.cnf用変数
if os.path.isfile(myconf_path):
    fo = open(myconf_path)
    alllines = fo.readlines()
    handshake = False
    pertable = False
    for strline in alllines:
        str_match = re.match('character-set-server\s*=\s*(.*)', strline.strip())
        if str_match is not None:
            result['VAR_Zabbix40SV_character_set_server'] = str_match.group(1).strip()
        str_match = re.match('skip-character-set-client-handshake', strline.strip())
        if str_match is not None:
            handshake = True
        str_match = re.match('innodb_file_per_table', strline.strip())
        if str_match is not None:
            pertable = True
        str_match = re.match('innodb_log_buffer_size\s*=\s*(.*)', strline.strip())
        if str_match is not None:
            result['VAR_Zabbix40SV_innodb_log_buffer_size'] = str_match.group(1).strip()
        str_match = re.match('innodb_buffer_pool_size\s*=\s*(.*)', strline.strip())
        if str_match is not None:
            result['VAR_Zabbix40SV_innodb_buffer_pool_size'] = str_match.group(1).strip()
        str_match = re.match('innodb_log_file_size\s*=\s*(.*)', strline.strip())
        if str_match is not None:
            result['VAR_Zabbix40SV_innodb_log_file_size'] = str_match.group(1).strip()
        str_match = re.match('innodb_log_files_in_group\s*=\s*(.*)', strline.strip())
        if str_match is not None:
            result['VAR_Zabbix40SV_innodb_log_files_in_group'] = int(str_match.group(1).strip())
        str_match = re.match('key_buffer_size\s*=\s*(.*)', strline.strip())
        if str_match is not None:
            result['VAR_Zabbix40SV_key_buffer_size'] = str_match.group(1).strip()
        str_match = re.match('max_allowed_packet\s*=\s*(.*)', strline.strip())
        if str_match is not None:
            result['VAR_Zabbix40SV_max_allowed_packet'] = str_match.group(1).strip()
    result['VAR_Zabbix40SV_skip_character_set_client_handshake'] = handshake
    result['VAR_Zabbix40SV_innodb_file_per_table'] = pertable
    fo.close()
# データベース設定用変数
zabbixServerConfMap_tmp = {
    "VAR_Zabbix40SV_DBName":"DBName",
    "VAR_Zabbix40SV_DBUser": "DBUser",
    "VAR_Zabbix40SV_DBPassword": "DBPassword",
    "VAR_Zabbix40SV_DBSocket": "DBSocket",
    "VAR_Zabbix40SV_LogFile": "LogFile",
    "VAR_Zabbix40SV_SocketDir": "SocketDir",
    "VAR_Zabbix40SV_AlertScriptsPath": "AlertScriptsPath",
    "VAR_Zabbix40SV_ExternalScripts": "ExternalScripts",
    "VAR_Zabbix40SV_SourceIP": "SourceIP",
    "VAR_Zabbix40SV_LogType": "LogType",
    "VAR_Zabbix40SV_DBHost": "DBHost",
    "VAR_Zabbix40SV_DBSchema": "DBSchema",
    "VAR_Zabbix40SV_HistoryStorageURL": "HistoryStorageURL",
    "VAR_Zabbix40SV_HistoryStorageTypes": "HistoryStorageTypes",
    "VAR_Zabbix40SV_ExportDir": "ExportDir",
    "VAR_Zabbix40SV_ExportFileSize": "ExportFileSize",
    "VAR_Zabbix40SV_JavaGateway": "JavaGateway",
    "VAR_Zabbix40SV_VMwareCacheSize": "VMwareCacheSize",
    "VAR_Zabbix40SV_SNMPTrapperFile": "SNMPTrapperFile",
    "VAR_Zabbix40SV_ListenIP": "ListenIP",
    "VAR_Zabbix40SV_CacheSize": "CacheSize",
    "VAR_Zabbix40SV_HistoryCacheSize": "HistoryCacheSize",
    "VAR_Zabbix40SV_HistoryIndexCacheSize": "HistoryIndexCacheSize",
    "VAR_Zabbix40SV_TrendCacheSize": "TrendCacheSize",
    "VAR_Zabbix40SV_ValueCacheSize": "ValueCacheSize",
    "VAR_Zabbix40SV_FpingLocation":	 "FpingLocation",
    "VAR_Zabbix40SV_Fping6Location": "Fping6Location",
    "VAR_Zabbix40SV_SSHKeyLocation": "SSHKeyLocation",
    "VAR_Zabbix40SV_TmpDir": "TmpDir",
    "VAR_Zabbix40SV_User": "User",
    "VAR_Zabbix40SV_SSLCertLocation": "SSLCertLocation",
    "VAR_Zabbix40SV_SSLKeyLocation": "SSLKeyLocation",
    "VAR_Zabbix40SV_SSLCALocation": "SSLCALocation",
    "VAR_Zabbix40SV_LoadModulePath": "LoadModulePath",
    "VAR_Zabbix40SV_TLSCAFile": "TLSCAFile",
    "VAR_Zabbix40SV_TLSCRLFile": "TLSCRLFile",
    "VAR_Zabbix40SV_TLSCertFile": "TLSCertFile",
    "VAR_Zabbix40SV_TLSKeyFile": "TLSKeyFile",
    "VAR_Zabbix40SV_Include": "Include",
    "VAR_Zabbix40SV_LoadModule": "LoadModule"
}
zabbixServerConfMap_tmp_int = {"VAR_Zabbix40SV_AllowRoot": "AllowRoot",
                               "VAR_Zabbix40SV_CacheUpdateFrequency": "CacheUpdateFrequency",
                               "VAR_Zabbix40SV_DBPort": "DBPort",
                               "VAR_Zabbix40SV_DebugLevel": "DebugLevel",
                               "VAR_Zabbix40SV_HistoryStorageDateIndex": "HistoryStorageDateIndex",
                               "VAR_Zabbix40SV_HousekeepingFrequency": "HousekeepingFrequency",
                               "VAR_Zabbix40SV_JavaGatewayPort": "JavaGatewayPort",
                               "VAR_Zabbix40SV_ListenPort": "ListenPort",
                               "VAR_Zabbix40SV_LogFileSize": "LogFileSize",
                               "VAR_Zabbix40SV_LogSlowQueries": "LogSlowQueries",
                               "VAR_Zabbix40SV_MaxHousekeeperDelete": "MaxHousekeeperDelete",
                               "VAR_Zabbix40SV_ProxyConfigFrequency": "ProxyConfigFrequency",
                               "VAR_Zabbix40SV_ProxyDataFrequency": "ProxyDataFrequency",
                               "VAR_Zabbix40SV_StartAlerters": "StartAlerters",
                               "VAR_Zabbix40SV_StartDBSyncers": "StartDBSyncers",
                               "VAR_Zabbix40SV_StartDiscoverers": "StartDiscoverers",
                               "VAR_Zabbix40SV_StartEscalators": "StartEscalators",
                               "VAR_Zabbix40SV_StartHTTPPollers": "StartHTTPPollers",
                               "VAR_Zabbix40SV_StartIPMIPollers": "StartIPMIPollers",
                               "VAR_Zabbix40SV_StartJavaPollers": "StartJavaPollers",
                               "VAR_Zabbix40SV_StartPingers": "StartPingers",
                               "VAR_Zabbix40SV_StartPollers": "StartPollers",
                               "VAR_Zabbix40SV_StartPollersUnreachable": "StartPollersUnreachable",
                               "VAR_Zabbix40SV_StartPreprocessors": "StartPreprocessors",
                               "VAR_Zabbix40SV_StartProxyPollers": "StartProxyPollers",
                               "VAR_Zabbix40SV_StartSNMPTrapper": "StartSNMPTrapper",
                               "VAR_Zabbix40SV_StartTimers": "StartTimers",
                               "VAR_Zabbix40SV_StartTrappers": "StartTrappers",
                               "VAR_Zabbix40SV_StartVMwareCollectors": "StartVMwareCollectors",
                               "VAR_Zabbix40SV_Timeout": "Timeout",
                               "VAR_Zabbix40SV_TrapperTimeout": "TrapperTimeout",
                               "VAR_Zabbix40SV_UnavailableDelay": "UnavailableDelay",
                               "VAR_Zabbix40SV_UnreachableDelay": "UnreachableDelay",
                               "VAR_Zabbix40SV_UnreachablePeriod": "UnreachablePeriod",
                               "VAR_Zabbix40SV_VMwareFrequency": "VMwareFrequency",
                               "VAR_Zabbix40SV_VMwarePerfFrequency": "VMwarePerfFrequency",
                               "VAR_Zabbix40SV_VMwareTimeout": "VMwareTimeout",
                               }
zabbixServerConfMap = {}
if os.path.isfile(zabbixServerConf_path):
    fo = open(zabbixServerConf_path)
    alllines = fo.readlines()
    installList = []
    loadModuleList = []
    for strline in alllines:
        if re.match('\s*#.*', strline) is not None:
            continue
        install_match = re.match('\s*Include\s*=(.*)', strline)
        if install_match is not None:
            installList.append(install_match.group(1).strip())
            continue
        loadModule_match = re.match('\s*LoadModule\s*=(.*)', strline)
        if loadModule_match is not None:
            loadModuleList.append(loadModule_match.group(1).strip())
            continue
        str_match = re.match('([^#]*)\s*=(.*)', strline)
        if str_match is not None:
            zabbixServerConfMap[str_match.group(1).strip()] = str_match.group(2).strip()
    fo.close()
    if len(installList) > 0:
        zabbixServerConfMap['Include'] = installList
    if len(loadModuleList) > 0:
        zabbixServerConfMap['LoadModule'] = loadModuleList
zabbixServerConfKeys = zabbixServerConfMap_tmp.keys()
for key in zabbixServerConfKeys:
    if zabbixServerConfMap_tmp[key] in zabbixServerConfMap:
        result[key] = zabbixServerConfMap[zabbixServerConfMap_tmp[key]]
zabbixServerConfKeys_int = zabbixServerConfMap_tmp_int.keys()
for key in zabbixServerConfKeys_int:
    if zabbixServerConfMap_tmp_int[key] in zabbixServerConfMap:
        if (zabbixServerConfMap[zabbixServerConfMap_tmp_int[key]] is not None) and (zabbixServerConfMap[zabbixServerConfMap_tmp_int[key]] != ''):
            result[key] = int(zabbixServerConfMap[zabbixServerConfMap_tmp_int[key]])

# WEBインターフェイス設定（PHP環境変数）
if os.path.isfile(zabbixConfPhp_path):
    fo = open(zabbixConfPhp_path)
    alllines = fo.readlines()
    for strline in alllines:
        str_match = re.match('\s*[$]ZBX_SERVER\s*=(.*)', strline)
        if str_match is not None:
            result['VAR_Zabbix40SV_ZBX_SERVER'] = str_match.group(1).strip().replace(';', '').replace("'", '').replace('"', '')
            continue
        str_match = re.match('\s*[$]ZBX_SERVER_PORT\s*=(.*)', strline)
        if str_match is not None:
            result['VAR_Zabbix40SV_ZBX_SERVER_PORT'] = int(str_match.group(1).strip().replace(';', '').replace("'", "").replace('"', ''))
            continue
        str_match = re.match('\s*[$]ZBX_SERVER_NAME\s*=(.*)', strline)
        if str_match is not None:
            result['VAR_Zabbix40SV_ZBX_SERVER_NAME'] = str_match.group(1).strip().replace(';', '').replace("'", '').replace('"', '')
    fo.close()

# WEBインターフェイス設定（Apache連携）
if os.path.isfile(zabbixConf_path):
    fo = open(zabbixConf_path)
    alllines = fo.readlines()
    isBegin = False
    for strline in alllines:
        str_match = re.match('\s*#.*', strline)
        if str_match is not None:
            continue
        str_match = re.match('\s*<IfModule\s*mod_php5.c\s*>\s*', strline)
        if str_match is not None:
            isBegin = True
        str_match = re.match('\s*</IfModule>\s*', strline)
        if str_match is not None:
            break
        if isBegin is True:
            str_match = re.match('\s*php_value\s*max_execution_time\s+(.*)', strline)
            if str_match is not None:
                result['VAR_Zabbix40SV_max_execution_time'] = int(str_match.group(1).strip())
                continue
            str_match = re.match('\s*php_value\s*memory_limit\s+(.*)', strline)
            if str_match is not None:
                result['VAR_Zabbix40SV_memory_limit'] = str_match.group(1).strip()
                continue
            str_match = re.match('\s*php_value\s*post_max_size\s+(.*)', strline)
            if str_match is not None:
                result['VAR_Zabbix40SV_post_max_size'] = str_match.group(1).strip()
                continue
            str_match = re.match('\s*php_value\s*upload_max_filesize\s+(.*)', strline)
            if str_match is not None:
                result['VAR_Zabbix40SV_upload_max_filesize'] = str_match.group(1).strip()
                continue
            str_match = re.match('\s*php_value\s*max_input_time\s+(.*)', strline)
            if str_match is not None:
                result['VAR_Zabbix40SV_max_input_time'] = int(str_match.group(1).strip())
                continue
            str_match = re.match('\s*php_value\s*always_populate_raw_post_data\s+(.*)', strline)
            if str_match is not None:
                result['VAR_Zabbix40SV_always_populate_raw_post_data'] = int(str_match.group(1).strip())
                continue
            str_match = re.match('\s*php_value\s*date.timezone\s+(.*)', strline)
            if str_match is not None:
                result['VAR_Zabbix40SV_date_timezone'] = str_match.group(1).strip()
                continue
    fo.close()

# ログローテート設定
if os.path.isfile(zabbixServer_path):
    fo = open(zabbixServer_path)
    alllines = fo.readlines()
    for strline in alllines:
        str_match = re.match('\s*(daily|weekly|monthly)\s*', strline)
        if str_match is not None:
            result['VAR_Zabbix40SV_RotateTiming'] = str_match.group(1).strip()
        str_match = re.match('\s*rotate\s+(.*)', strline)
        if str_match is not None:
            result['VAR_Zabbix40SV_RotateCount'] = int(str_match.group(1).strip())
    fo.close()
print(json.dumps(result))