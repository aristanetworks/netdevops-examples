# LAB 02 - CloudVision Collection overview

## About

Basic commands to test ansible with a basic installation.

## Execute lab

__1. Install `arista.cvp` collection.__

```shell
# Install documentation.
$ ansible-galaxy collection install arista.cvp:==1.0.4 -p ../collections/

# Display module documentation.
$ ansible-doc arista.cvp.cv_device
```

__2. Collect facts from CloudVision.__

```shell
$ ansible-playbook playbook.facts.yml
```

__3. Optional: Collect only facts for devices__

Get and display facts of active devices with their configuration.

```yaml
- name: "Gather CVP facts {{inventory_hostname}}"
    arista.cvp.cv_facts:
    facts:
        devices
    gather_subset:
        config
    register: cv_facts
```
