import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_mysql_installed(host):
    mysql = host.package('mysql-server-5.7')
    assert mysql.is_installed
    assert mysql.version.startswith('5.7')


def test_config_file(host):
    config_file = host.file("/etc/mysql/my.cnf")
    assert config_file.user == 'root'
    assert config_file.group == 'root'
    assert config_file.mode == 0o644
