# LAB 01 - Ansible Basics

## About

Basic commands to test ansible with a basic installation.


## Execute lab

__1. Test Ansible installation__

```shell
$ ansible 127.0.0.1 -m ping
[WARNING]: No inventory was parsed, only implicit localhost is available

127.0.0.1 | SUCCESS => {
    "changed": false,
    "failed": false,
    "ping": "pong"
}
```

__2. Display variables for a given host__

```shell
$ ansible DC-LEAF1A -m debug -a "var=hostvars[inventory_hostname]"
```

