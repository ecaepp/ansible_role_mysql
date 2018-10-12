ansible_role_mysql
=========

This role will install a vary baseline Mysql server for Ubuntu-16.04

Requirements
------------

Ansible

Role Variables
--------------

Currently variables for username and password are set in `defaultes/mail.yml`. These can easily be orver written by recreateing the variables in `vars/main.yml`.

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
