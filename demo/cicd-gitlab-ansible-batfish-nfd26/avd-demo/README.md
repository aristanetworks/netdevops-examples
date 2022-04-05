![](https://img.shields.io/badge/Arista-CVP%20Automation-blue) ![](https://img.shields.io/badge/Arista-EOS%20Automation-blue) ![Ansible Code Execution](https://github.com/arista-netdevops-community/ansible-avd-cloudvision-demo/workflows/Ansible%20Code%20Execution/badge.svg) ![GitHub](https://img.shields.io/github/license/arista-netdevops-community/ansible-avd-cloudvision-demo)
# Arista Validated Design with CloudVision deployment

## About

This example implement a basic __EVPN/VXLAN Fabric__ based on __[Arista Validated Design roles](https://github.com/aristanetworks/ansible-avd)__ with one layer of 2 spines and one layer of leafs (4 devices) using MLAG. Configuration deployment is not managed by eos EAPI, but through Arista CloudVision based on __[arista.cvp collection](https://github.com/aristanetworks/ansible-cvp/)__

It helps to demonstrate how to bring up an Arista EVPN/VXLAN Fabric from the first boot.

![Lab Topology](data/cloudvision-device-topology.png)

> Lab is based on EVE-NG topology and a CloudVision server running on a VMware instance. A complete guide to setup Arista EOS devices on EVE is available on [AVD website](https://avd.sh/en/latest/docs/how-to/lab-with-nat/)

## Getting Started

For detailed setup and demo, please refer to [resources](#resources) below.

> It is recommended to use [docker image](https://hub.docker.com/repository/docker/avdteam/base) with all [arista.cvp](https://github.com/aristanetworks/ansible-cvp) and [arista.avd](https://github.com/aristanetworks/ansible-avd) [requirements](https://avd.sh/en/latest/docs/installation/requirements/). It is done with `make shell` command.

```shell
# Clone repository
$ git clone https://github.com/arista-netdevops-community/ansible-avd-cloudvision-demo.git

# Move to folder
$ cd ansible-avd-cloudvision-demo

# Run demo shell using docker (optional)
$ make shell

# Install required ansible collections
$ ansible-galaxy collection install arista.avd:==2.0.0
$ ansible-galaxy collection install arista.cvp:==2.1.2

# Edit Inventory information & Authentication information
$ vim inventory/inventory.yml

# Edit ZTP information
$ vim inventory/group_vars/CVP.yml

# Provision Zero Touch Provisioning server
$ ansible-playbook playbooks/dc1-ztp-configuration.yml

# Power Up devices
# Wait for devices to be available in CVP

# Run Ansible playbook
$ ansible-playbook playbooks/dc1-fabric-deploy-cvp.yml
```

> Getting started does not include management IP configuration. For complete installation, please refer to [installation guide](INSTALLATION.md) to configure correct environment.

## Resources

- Ansible [Arista Validated Design](https://github.com/aristanetworks/ansible-avd) repository.
- [Ansible CloudVision Collection](https://github.com/aristanetworks/ansible-cvp) repository.
- [How to install](INSTALLATION.md) demo environment.
- [Detailed demo script](DEMO.md).

## License

Project is published under [Apache License](LICENSE).
