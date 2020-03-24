# LAB 03 - Manage Configlet on Cloudvision.

## About

Create, Update and Delete configlets on CloudVision.

## Execute lab

__1. Review configlet vars__

```shell
$ cat group_vars/CVP.yml

---
CVP_CONFIGLETS:
  01TRAINING-alias: "alias a{{ 999 | random }} show version"
  01TRAINING-01: "alias a{{ 999 | random }} show version"
```

__2. Create 2 new configlets on CloudVision server.__

```shell
$ ansible-playbook playbook.configlet.yml
```

__3. Optional: Add a new configlet from file__

Create configlet with content of file [configlet.txt](configlet.txt)

Edit [CVP.yml](group_vars/CVP.yml) file

```
$ vim group_vars/CVP.yml
```

And update content with

```yaml
---
CVP_CONFIGLETS:
  01TRAINING-alias: "alias a{{ 999 | random }} show version"
  01TRAINING-01: "alias a{{ 999 | random }} show version"
  01TRAINING-02: "{{lookup('file', '../configlet.txt')}}"
```

Run playbook and check on CloudVision

__4. Remove configlet 01TRAINING-01 from CloudVision__

Edit [CVP.yml](group_vars/CVP.yml) file

```
$ vim group_vars/CVP.yml
```

And update content with

```yaml
---
CVP_CONFIGLETS:
  01TRAINING-alias: "alias a{{ 999 | random }} show version"
```

Run playbook and check on CloudVision

__5. Remove all configlets created in this lab__

- Edit playbook
- Set mode to absent
- Run playbook
