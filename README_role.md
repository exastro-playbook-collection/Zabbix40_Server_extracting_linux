# Zabbix Server 収集ロール

# Trademarks
-----------
* Linuxは、Linus Torvalds氏の米国およびその他の国における登録商標または商標です。
* RedHat、RHEL、CentOSは、Red Hat, Inc.の米国およびその他の国における登録商標または商標です。
* Windows、PowerShellは、Microsoft Corporation の米国およびその他の国における登録商標または商標です。
* Ansibleは、Red Hat, Inc.の米国およびその他の国における登録商標または商標です。
* pythonは、Python Software Foundationの登録商標または商標です。
* Zabbixは、ラトビア共和国にあるZabbix LLCの商標です。
* Oracleは、Oracle International Corporation の米国およびその他の国における登録商標または商標です。
* NECは、日本電気株式会社の登録商標または商標です。
* その他、本ロールのコード、ファイルに記載されている会社名および製品名は、各社の登録商標または商標です。

## Description

本ロールでは、Zabbix Server構築済み環境から設定情報を収集する機能と、収集した設定情報からZabbix Server構築ロール([linux版])で使用できるパラメータを生成する機能を提供します。

## Supports

本ロールは、以下環境をサポートします。

- 管理サーバー（Ansible実行サーバー）
  - OS：RHEL7.4（CentOS7.4）/RHEL8.0（CentOS8.0）
  - Ansible：Version 2.8
  - Python：2.7 or 3.6
- 対象サーバー
  - 利用しているロール、共通部品の仕様に準拠します。

## Dependencies

本ロールでは、以下のロール、共通部品を利用しています。

- 収集機能（Zabbix40_Server_gathering_linux）
  - gathering ロール

- パラメータ生成機能（Zabbix40_Server_extracting_linux）
  - パラメータ生成共通部品

## Role Variables

本ロールで指定できる変数値について説明します。

### Mandatory Variables

ロール利用時に必ず指定しなければならない変数値はありません。

### Optional Variables

ロール利用時に以下の変数値を指定することができます。

- 共通

    | Name                            | Default Value | Description                        |
    | ------------------------------- | ------------- | -----------------------------------|
    |`VAR_Zabbix40_Server_linux_gathering_dest` |'{{ playbook_dir }}/_gathered_data' |収集した設定情報の格納先パス |

- Zabbix40_Server_gathering_linux

    | Name                            | Default Value | Description                        |
    | ------------------------------- | ------------- | -----------------------------------|
    |`VAR_Zabbix40SV_localpkg_dst`    |'/tmp' |構築対象サーバ上の「php-bcmath」および「php-mbstring」ファイルのコピー先フォルダ |
    |`VAR_Zabbix40SV_localpkg_src`    |'/tmp' |管理サーバ上の「php-bcmath」および「php-mbstring」ファイルのコピー元フォルダ |

- Zabbix40_Server_extracting

    | Name                             | Default Value | Description                        |
    | -------------------------------- | ------------- | -----------------------------------|
    |`VAR_Zabbix40_Server_linux_extracting_rolename` |'['Zabbix40-Server_install','Zabbix40-Server_setup','Zabbix40-Server_ossetup']'  |パラメータ生成対象 |
    |`VAR_Zabbix40_Server_linux_extracting_dest` |"{{ playbook_dir }}/_parameters"     |生成したパラメータの出力先パス |

## Results

本ロールの出力について説明します。

### 収集した設定情報の格納先

収集した設定情報は以下のディレクトリ配下に格納します。

-  {{ VAR_Zabbix40_Server_linux_gathering_dest }}/{{ inventory_hostname }}/Zabbix40_Server_gathering_linux/

本ロールをデフォルト設定で利用した場合、以下のように設定情報を格納します。

- linux版 Zabbix Server の場合

    ```none
    <Playbook実行ディレクトリ>/
      +-_gathered_data/
          +-<ホスト名/IP>/
              +-Zabbix40_Server_gathering_linux/         # 収集データ
                  +-command/
                      ：
    ```

### 生成したパラメータの出力例

生成したパラメータは以下のディレクトリ・ファイル名で出力します。

- {{ VAR_Zabbix40_Server_linux_extracting_dest }}/{{ inventory_hostname }}/{{ VAR_Zabbix40_Server_linux_extracting_rolename }}.yml

本ロールをデフォルト設定で利用した場合、以下のようにパラメータを出力します。

- Zabbix Server の場合

    ```none
    <Playbook実行ディレクトリ>/
      +-_parameters/
          +-<ホスト名/IP>/
              +-Zabbix40-Server_install.yml               # パラメータ
              +-Zabbix40-Server_setup.yml                 # パラメータ
              +-Zabbix40-Server_ossetup.yml               # パラメータ
    ```

## Usage

本ロールの利用例について説明します。

### 設定情報収集およびパラメータ生成を行う場合

以下の例ではデフォルト設定で設定情報収集およびパラメータ生成を行います。

- `Zabbix40_Server_extracting.yml` (Zabbix Server用Playbook)

    ```yaml
    ---
    - hosts: linux
      become: no
      roles:
        - role: Zabbix40_Server_gathering_linux
        - role: Zabbix40_Server_extracting_linux
    ```

- 以下のように設定情報とパラメータを出力します。

    ```none
    <Playbook実行ディレクトリ>/
      +-_gathered_data/
      |   +-<ホスト名/IPアドレス>/
      |       +-Zabbix40_Server_gathering_linux/          # 収集データ
      |           +-command/
      |               ：
      +-_parameters/
          +-<ホスト名/IPアドレス>/
              +-Zabbix40-Server_install.yml               # パラメータ
              +-Zabbix40-Server_setup.yml                 # パラメータ
              +-Zabbix40-Server_ossetup.yml               # パラメータ
    ```

### パラメータ再利用

以下の例では、生成したパラメータを使用して構築済Zabbix Server Ver4.0の設定を変更します。

- `Zabbix_Server_setup.yml`（Zabbix Server構築ロールを使用）

    ```yaml
    ---
    - hosts: linux
      roles:
        - Zabbix40-Server_setup
    ```

- 生成したパラメータを指定してplaybookを実行

    ```sh
    ansible-playbook Zabbix_Server_setup.yml -i hosts --extra-vars="@_parameters/<ホスト名/IPアドレス>/Zabbix40-Server_setup.yml"
    ```

# Copyright
Copyright (c) 2019 NEC Corporation

# Author Information
NEC Corporation
