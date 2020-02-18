![](https://img.shields.io/badge/Arista-CVP%20Automation-blue) ![](https://img.shields.io/badge/Arista-EOS%20Automation-blue)
# Arista Validated Design with CloudVision deployment & Zero Touch Provisioning.

## About

This example implement a basic __EVPN/VXLAN Fabric__ based on __[Arista Validated Design roles](https://github.com/aristanetworks/ansible-avd)__ with one layer of 2 spines and one layer of leafs (4 devices) using MLAG. Configuration deployment is not managed by eos EAPI, but through Arista CloudVision based on __[arista.cvp collection](https://github.com/aristanetworks/ansible-cvp/)__

It helps to demonstrate how to bring up an Arista EVPN/VXLAN Fabric from the first boot.

![Lab Topology](data/cloudvision-device-topology.png)

> Lab is based on GNS3 topology and a CloudVision server running on a VMware instance.

## Getting Started

For detailled setup and demo, please refer to [ressources](#ressources) below.

```shell
# Clone repository
$ git clone https://github.com/aristanetworks/netdevops-examples.git

# Move to folder
$ cd netdevops-examples/ansible/ztp-avd-cvp

# Install python requirements
$ pip install -r requirements.txt

# Install required ansible collections
$ make install

# Edit ZTP information
$ vim dc1-ztp-configuration.yml

# Provision Zero Touch Provisioning server
$ ansible-playbook dc1-ztp-configuration.yml

# Power Up devices
# Wait for devices to be available in CVP

# Run Ansible playbook 
$ ansible-playbook dc1-fabric-deploy-cvp.yml
```

> Getting started does not include management IP configuration. For complete installation, please refer to [installation guide](INSTALLATION.md) to configure correct environment.

## Ressources

- Ansible [Arista Validated Design](https://github.com/aristanetworks/ansible-avd) repository.
- Ansible [CloudVision Collection](https://github.com/aristanetworks/ansible-cvp) repository.
- [How to install](INSTALLATION.md) demo environment.
- [Detailled demo script](DEMO.md).
- [Detailled demo script with docker](data/DEMO_DOCKER.md)

## License

Project is published under [Apache](../../LICENSE).
