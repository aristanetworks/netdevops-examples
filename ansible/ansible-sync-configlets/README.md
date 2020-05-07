![](https://img.shields.io/badge/Arista-CVP%20Automation-blue) ![License](https://img.shields.io/github/license/aristanetworks/ansible-cvp)

# Synchronizing Arista CloudVision Portal Configlets across multiple Platforms

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

<!-- /code_chunk_output -->

## About

[Arista Networks](https://www.arista.com/) supports Ansible for managing devices running the EOS operating system through [CloudVision platform (CVP)](https://www.arista.com/en/products/eos/eos-cloudvision). This lab will explore the use of the modules to synchronise a designated set of CVP Configlets across multiple CVP instances.  The aim will be to deploy and synchronise a set of configlets that could be updated from any instance of CVP or via an Ansible PlayBook. This provides a flexible method of managing the configlets without imposing any requirements to exclusively use either CVP or Ansible for updating them.

<p align="center">
  <img src='docs/cv_ansible_logo.png' alt='Arista CloudVision and Ansible'/>
</p>

## Lab overview

In this lab Ansible 2.9.2 was installed in to a virtual python environment running python 2.7.9 although the modules have also been tested with python 3.x. To create the virtual environment and install Ansible and any required modules the following commands were used. The commands were issued from the directory in which the lab was to be executed. In this case it was in a directory called “Ansible_Sync_CVP”:

```shell
> pwd
~/Ansible_Sync_CVP
> virtualenv --no-site-packages -p $(which python2.7) .venv
> source .venv/bin/activate
> pip install --user ansible
> pip install netaddr requests treelib
> ansible-galaxy collection install arista.cvp
```
In addition to the above packages SSHPASS will also be required, this can be installed using one of the following methods depending on the Operating System of the Ansible host:

```shell
UBUNTU:
> apt-get install sshpass

MACOS:
> brew install https://raw.githubusercontent.com/kadwanev/bigboybrew/master/Library/Formula/sshpass.rb
```

__Important note:__

This repository is built based on [new collections system](https://docs.ansible.com/ansible/devel/dev_guide/developing_collections.html#developing-collections) introduced by ansible starting version __2.9__. 

> It means that it is required to run at least ansible `2.9.0rc4` to be able to use this collection.


Once the lab has been installed the Ansible configuration file ansible.ini will need to be updated

Having configured Ansible to enable access to the CVP servers two roles are required for the PlayBooks, these roles will be created in a subdirectory called roles:

```shell
> pwd
~/Ansible_Sync_CVP 

> mkdir ./roles
> ansible-galaxy init ./roles/cvp.sync
- Role ./roles/cvp.sync was created successfully
> ansible-galaxy init ./roles/cvp.refresh
- Role ./roles/cvp.refresh was created successfully
```
The role directories contain a template structure for the two Ansible roles required.

A set of directories and data stores are required to store the variables created and used by the PlayBook. These data stores are in the form of YAML files and located in a directory structure under generated_vars:

```shell
> pwd
~/Ansible_Sync_CVP 

> mkdir ./generated_vars
> mkdir ./generated_vars/common_configlets
> mkdir ./generated_vars/containers
> mkdir ./generated_vars/cvp_servers
```
The __common_configlets__ directory contains details of the configlets that are to be synchronised across the CVP instances.

The __containers__ directory contains details of the provisioning hierarchies for each CVP server in order to be able to deploy the synchronized (shared) configlets on each CVP server.

The __cvp_servers__ directory contains details of which configlets are to be deployed to the CVP servers. This directory can be used by other PlayBooks to deploy configlets and provision devices.

The __group_vars__ directory is used to share data between Ansible roles.

## Ansible Playbook - cvp.sync.yml

The Ansible playbook cvp.sync.yml consists of two plays that import the following roles:

### cvp.sync

  __cvp.sync__ connects to each of the CVP instances, locates the configlets with “shared_” in their name and updates the shared Configlet data (config, last time changed, associated containers, associated devices) for each CVP instance. This data is stored in the generated_vars directory as a YAML file with the CVP instance name.

### cvp.refresh

 __cvp.refresh__ connects to each of the CVP instances and updates the shared configlets on each one using the information provided by cvp.sync

### cvp.sync.yml

__cvp.sync.yml__ conists of two plays:

#### Check Shared Configlets across CVP clusters 
 imports the the cvp.sync role and runs it against each CVP server in turn. Unlike other plays this play serialises the execution of the role for each CVP server. This means that cvp_server_1 has to complete before the playbook will move onto cvp_server_2. This avoids a race condition where both CVP server plays try to update the master.yml file at the same time. If this happens they will not compare Configlet time stamps correctly. This race condition can cause the wrong Configlets (not the latest) to be stored in the file.

#### Update Shared Configlets across CVP clusters
 imports the cvp.refresh role and uses it to push configlet updates to each of the CVP servers. This play runs in parallel allowing both CVP servers to be updated simultaneously.

## Lab Execution

When the playbook is executed using the “check” flag it will gather the shared Configlet information and update the master.yml file.

```shell
> pwd
~/Ansible_Sync_CVP 
> ansible-playbook ./cvp.sync.yml --tags check
PLAY [Check Shared Configlets across CVP clusters]
...
```

When the playbook is executed using the “sync” flag it will gather the shared Configlet information and update the master.yml file then synchronize the Configlets across the CVP instances.

```shell
> pwd
~/Ansible_Sync_CVP 
> ansible-playbook ./cvp.sync.yml --tags sync
PLAY [Check Shared Configlets across CVP clusters]
...
PLAY [Update Shared Configlets across CVP clusters]
...
```

The Configlets can then be changed on either CVP instance or by manipulating the master.yml file and the playbook executed again using the “sync” flag. With each execution the master.yml file is updated and the latest version of the shared Configlets is pushed to each of the CVP instances.

## Resources

A full write up of this lab is provided on Arista EOS Central:
[Synchronising CloudVision Portal Configlets with Ansible](https://eos.arista.com/synchronising-cloudvision-portal-configlets-with-ansible/)


## License

This project is published under [Apache License](LICENSE).

## Ask a question

Support for the `arista.cvp` collection is provided by the community directly in the [aristanetworks/ansible-cvp](https://github.com/aristanetworks/ansible-cvp) repository. Easiest way to get support is to open [an issue](https://github.com/aristanetworks/ansible-cvp/issues).

To ask a question about this lab please "Ask a Question" in the [Arista EOS Central Forum](https://eos.arista.com/forum/)
