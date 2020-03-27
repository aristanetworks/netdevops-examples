# Tech Friday Ansible CVP Collection demo

## About

Lorem Ipsum

## Demo run:

### Publish 2 configlets to CVP using arista.cvp collection

- Configlets are available under [`configlets/`](configlets/)
- Data structure to use to update CVP: [`group_vars/CVP.yml`](group_vars/CVP.yml)

```yaml
cvp_raw_configlets:
    CVP_RAW_DEMO_ADMIN_USERS: "{{lookup('file', 'configlets/ADMIN_USERS.conf')}}"
    CVP_RAW_DEMO_ALIASES: "{{lookup('file', 'configlets/ALIASES.conf')}}"
```

- Playbook using `arista.cvp.cv_configlet` module

```yaml
- name: 'create configlets on CVP {{inventory_hostname}}.'
    arista.cvp.cv_configlet:
    cvp_facts: "{{CVP_FACTS.ansible_facts}}"
    configlets: "{{cvp_raw_configlets}}"
    configlet_filter: ["{{ configlets_cvp_raw_prefix }}"]
    register: CONFIGLET_UPDATE
```


### Publish configlets from a folder to Cloudvision

- Configlets are available under [`configlets/`](configlets/)
- Instruct role where to find configlets in [`group_vars/CVP.yml`](group_vars/CVP.yml)

```yaml
configlets_prefix_var: "CV_DEMO"
configlet_dir_var: "configlets/"
```

- Use role in a playbook:

```yaml
- name: 'upload configlets from cloudvision {{inventory_hostname}}'
    import_role:
      name: arista.avd.cvp_configlet_upload
    vars:
      configlet_directory: '{{ configlet_dir_var }}'
      configlets_cvp_prefix: '{{ configlets_prefix_var }}'
```
