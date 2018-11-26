[![Build Status](https://travis-ci.com/ecaepp/ansible_role_mysql.svg?branch=master)](https://travis-ci.com/ecaepp/ansible_role_mysql)
<!---
# Commented out until further testing can be done to see if this will work for ansbile roles.
[![Coverage Status](https://coveralls.io/repos/github/ecaepp/ansible_role_mysql/badge.svg?branch=master)](https://coveralls.io/github/ecaepp/ansible_role_mysql?branch=master)
--->

ansible_role_mysql
=========

This role will install a baseline Mysql server 5.7 and go though the steps for secure setup. This role will also create `/ect/mysql/my.cnf` with basic configuration to get the server up and running.

Requirements
------------

Ansible

Role Variables
--------------

Currently variables to set options such as username, password, logging, InnoDB, and general setting are set in `defaultes/mail.yml`. Setting var in `defaults/main.yml` allow for the variables to easly be overwritten else in the ansible-playbook.
See link for [Ansible variable precedence](https://docs.ansible.com/ansible/2.5/user_guide/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable).

Dependencies
------------
None.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: ecaepp.ansible_role_mysql }

License
-------

GPLv3

Author Information
------------------

Automation enthusiest wanting to start creating and sharing.
