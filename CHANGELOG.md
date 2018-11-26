
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.4.4] - 2018-11-26


## [1.4.3] - 2018-11-26

### Change

6b25cb4 [CHANGE] Added `latest` tag to docker image. (ecaepp)

### Fix

f6f9b1c [FIX] Commented out matrix envar (ecaepp)

## [1.4.0] - 2018-11-12

### Added

- 5eabac6 [ADDED] Task to create system account. (ecaepp)
- e347d28 [ADDED] Task to create database accounts. (ecaepp)
- c124a20 [ADDED] Tasks to create database and accounts. (ecaepp)
- 129b052 [ADDED] `MySQL` to task names. (ecaepp)
- fcb4f2a [ADDED] Home directory var fo mysql user. (ecaepp)
- 73b52e8 [ADDED] Task for creating database. (ecaepp)
- e59d2c8 [ADDED] Database settings. (ecaepp)
- 5bf8186 [ADDED] Task to create my.cnf file from templates. (ecaepp)
- 1db0ee6 [ADDED] Pre tasks to check MySQL binary exisits. (ecaepp)
- c544122 [ADDED] Task to include `configuration.yml` (ecaepp)
- fe84037 [ADDED] `pre_tasks` include and conditaional for Debian install. (ecaepp)
- 99d2401 [ADDED] `changed_when` conditional to fix impotdence. (ecaepp)
- 215cbb4 [ADDED] defined test sequence (ecaepp)
- 50ae775 [ADDED] my.cnf example file (ecaepp)
- 1e1282b [ADDED] changelog (ecaepp)
- 37d2d3c [ADDED] files for root and user (ecaepp)
- 92fe658 [ADDED] tasks to set MySQL default password using debconf (ecaepp)
- 30c76bb [ADDED] to  configs (ecaepp)
- 530db83 [ADDED] task (ecaepp)
- 30d3b9c [ADDED] tasks file (ecaepp)
- 7d8eabf [ADDED] to deploy config (ecaepp)

### Changed

- b7a608c [CHANGE] mysql user name (ecaepp)
- 1420b16 [CHANGE]  Mysql user vars. (ecaepp)
- bd3b811 [CHANGE] Moved tasks to `secure_setup`. (ecaepp)
- 0dbd919 [CHANGE] Renamed task to `secure_setup.yml`. (ecaepp)
- 80e48a7 [CHANGE] Moved `copy root my.cnf file` to `configuration.yml`. - (ecaepp)
- 44eab94 [CHANGE] Renamed `configure_users.yml` to `secure_setup.yml`. - (ecaepp)
- 5f92363 [CHANGE] Moved `debconf` tasks to `Debian_install.yml. (ecaepp)
- e7cdc10 [CHANGE] role name in playbook.yml (ecaepp)
- cec7855 [CHANGE] Mysql user/root vars. (ecaepp)
- c41a0e1 [CHANGE] task  to (ecaepp)
- d51f655 [CHANGE] out install tasks (ecaepp)
- fa5c3d4 [CHANGE] my.cnf location to /etc/mysql/conf.d (ecaepp)

### Fixed

- 26f8c0d [FIX] Syntax issue. (ecaepp)
- 6d99b5a [FIX] Removed trailing space. (ecaepp)
- b3b0f92 [FIX] spacing (ecaepp)
- f7fdb2a [FIX] multiple variable bugs cauing failures (ecaepp)
- b854722 [FIX] option name (ecaepp)

### Removed

- 74fc934 [REMOVED] Code that was moved to `configuration.yml`. (ecaepp)
- 986a51f [REMOVED] debug code. (ecaepp)
- 44fd968 [REMOVED] Removed task `Restart MySQL` to fix idempotence. (ecaepp)
- 66959cd [REMOVED] uneeded code (ecaepp)

### Documentation

- 64580e7 [DOC] Added variable comments. (ecaepp)
