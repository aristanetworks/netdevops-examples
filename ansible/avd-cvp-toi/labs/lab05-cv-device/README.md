# LAB 05 - Manage device on CloudVision

## About

Manage configlets attached to a device.

## Execute lab

__1. Review configlet vars__

```yaml
$ cat group_vars/CVP.yml

---
CVP_DEVICES:
  leaf1:
    name: 'leaf1'
    parentContainerName: Leaf
    configlets:
        - 'Leaf1-BGP-Lab'
        - 'BaseIPv4_Leaf1'
    imageBundle: []  # Not yet supported
```

__2. Attach configlet `Leaf1-BGP-LAB` to leaf1 device.__

```shell
$ ansible-playbook playbook.device.yml
```

__3. Optional: Create new configlets and attach them to leaf1__

```shell
$ cat group_vars/CVP.yml

---
CVP_CONFIGLETS:
  01TRAINING-alias: "alias a{{ 999 | random }} show version"
  01TRAINING-01: "alias a{{ 999 | random }} show version"

CVP_DEVICES:
  leaf1:
    name: 'leaf1'
    parentContainerName: Leaf
    configlets:
        - 'Leaf1-BGP-Lab'
        - 'BaseIPv4_Leaf1'
        - '01TRAINING-01'
    imageBundle: []  # Not yet supported
```

Update playbook accordingly.