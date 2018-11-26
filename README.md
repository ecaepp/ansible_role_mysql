[![Build Status](https://travis-ci.com/ecaepp/ansible_role_mysql.svg?branch=master)](https://travis-ci.com/ecaepp/ansible_role_mysql)
<!---
# Commented out until further testing can be done to see if this will work for ansbile roles.
[![Coverage Status](https://coveralls.io/repos/github/ecaepp/ansible_role_mysql/badge.svg?branch=master)](https://coveralls.io/github/ecaepp/ansible_role_mysql?branch=master)
--->

# ansible_role_mysql

## Overview

This role will install a baseline Mysql server 5.7 and go though the steps for secure setup. This role will also create `/ect/mysql/my.cnf` with basic configuration to get the server up and running.

## Requirements

Ansible

## Role Variables

Variables are use to define configable options for MSQL. Currently variables to set options such as username, password, logging, InnoDB, and general setting are set in `defaultes/mail.yml`. Setting var in `defaults/main.yml` allow for the variables to easly be overwritten else in the ansible-playbook.
See link for [Ansible variable precedence](https://docs.ansible.com/ansible/2.5/user_guide/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable).

### Root User settings

```yml
mysql_root_default_password: p@$$w0rD1!
mysql_root_password: "{{ mysql_root_default_password }}"
mysql_root_username: root
```

By default this role sets the `mysql_root_password` to `mysql_root_default_password` this generally fine for local testing but should be changed for production. Best practice would be to use Ansible Vault to store any passwords encrypted.

### MySQL User Settings

```yml
mysql_user_username: root
mysql_user_password:
mysql_user_group: root
mysql_user_home_dir: /home/{{ mysql_user_username}}
```

These settings are for the local admin account for the MySQL and defaults to the installation default of root. Changing the settings willcause the role to create a new system account and configures the account without login premissions.

#### Example:

```yml
mysql_user_username: mysql
mysql_user_password: mysqlpassword
mysql_user_group: mysql
mysql_user_home_dir: /home/{{ mysql_user_username}}
```

Would create a system account and group `mysql` and prevent the account from being able to login to the system by setting its shell to `/usr/sbin/nologin`.

The following vars are used to configure the MySQL service at `/etc/mysql`.

#### client:

```yml
mysql_port: 3306
mysql_socket: /var/lib/mysql/mysql.sock
```

Default MySQL port and location for socket.

#### mysqld:

##### General Settings

```yml
mysql_user: mysql
default_storage_engine: InnoDB
pid_file: /var/lib/mysql/mysql.pid
```

##### MyISAM Settings

```yml
key_buffer_size: 32M
myisam_recover_options: FORCE,BACKUP
```

##### Safety

```yml
max_allowed_packet: 16M
max_connect_errors: 10000000
sql_mode: STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_AUTO_VALUE_ON_ZERO,NO_ENGINE_SUBSTITUTION,NO_ZERO_DATE,NO_ZERO_IN_DATE,ONLY_FULL_GROUP_BY
sysdate_is_now: 1
innodb: FORCE
```

##### Data Storage

```yml
data_dir: /var/lib/mysql
```

##### Binnary logging

```yml
server_id: 1
log_bin: /var/log/mysql/mysql_bin
expire_logs_days: 14
sync_binlog: 1
```

##### Cache and Limits

```yml
tmp_table_size: 32m
max_heap_table_size: 32M
query_cache_type: 0
query_cache_size: 0
max_connections: 500
thread_cache_size: 50
open_files_limit: 65535
table_definition_cache: 1024
table_open_cache: 512
```

##### InnoDB

```yml
innodb_flush_method: O_DIRECT
innodb_log_files_in_group: 2
innodb_log_file_size: 256M
innodb_flush_log_at_trx_commit: 1
innodb_file_per_table: 1
innodb_buffer_pool_size: 12G
```

##### Logging

```yml
log_error: /var/lib/mysql/mysql_error.log
log_queries_not_using_indexes: 1
slow_query_log: 1
slow_query_log_file: /var/lib/mysql/mysql_slow.log
```

The following configs are for setting up databases in MySQL. Multiple DBs can be defined using YAML array.

When ran defautly the role will initialize an empty arry that triggers a conditional to skip the task that create any databases.

##### Database setup

```yml
mysql_database: []
#  - name: example
#  - collation: utf8_general_ci
#  - encoding: utf-8
#  - replicate: 1
```

These setting can be used to setup, remove,  or modify any MySQL application or DBA accounts in MySQL and grant or remove premissions to databases and tables.

##### MySQL users

```yml
mysql_users: []
# - host: myuser
# - password: somepassword
# - priv: my_db.*:ALL
# - state: present
# - append_privs: no
# - encrypted: no
```

## Dependencies

None.

#### Example Playbook

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: ecaepp.ansible_role_mysql }

## License


GPLv3

## Author Information

Automation enthusiest wanting to start creating and sharing. 