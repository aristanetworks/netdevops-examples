
# Demo script

- [Demo script](#demo-script)
  - [Power up devices.](#power-up-devices)
  - [Run Ansible playbook to rollout EVPN Fabric](#run-ansible-playbook-to-rollout-evpn-fabric)
    - [Playbook overview](#playbook-overview)
    - [Run Playbook](#run-playbook)
      - [Generate EOS Configuration](#generate-eos-configuration)
      - [Provision CloudVision Server](#provision-cloudvision-server)
      - [Execute Pending tasks using a change control](#execute-pending-tasks-using-a-change-control)
  - [Analyze result.](#analyze-result)
    - [Topology Update](#topology-update)
    - [Configlet list](#configlet-list)
    - [Check device status](#check-device-status)
    - [Check device connectivity](#check-device-connectivity)
  - [Revert topology](#revert-topology)

## Power up devices.

Power up your devices what ever the solution is. You will see them in the __`undefined`__ container

![ZTP Registration](data/cloudvision-ztpd-devices.png)

__Check there is no container__

![Streaming Inventory](data/streaming-inventory.png)


__Check Configlets are not present__

![Configlets](data/cloudvision-initial-configlet.png)

> CloudVision might have some configlets, but not configlets with AVD related content.

## Run Ansible playbook to rollout EVPN Fabric

A set of tags are available, but it is recommended to execute playbook in a row:

### Playbook overview

Playbook: [`dc1-fabric-deploy-cvp.yml`](dc1-fabric-deploy-cvp.yml)

Playbook manage following actions:
- Generate Variables for CVP structure:
    - List of configlets
    - Containers topology
    - List of devices.
- Collect CloudVision Facts
- Deploy Configlet to CloudVision
- Build Containers Topology
- Configure devices with correct configlet and container.
- Execute created tasks (wait 5 minutes while devices reboot)

This playbook supports 2 tags to run demo step by step:
- __build__: Generate configuration.
- __provision__: Push content to CloudVision.

### Run Playbook

#### Generate EOS Configuration

Use tag `build` to only generate 
- [EOS structured configuration(YAML)](intended/structured_configs/)
- [EOS configuration](intended/configs/)
- [EOS Documentation](documentation/)
- CloudVision parameters

```shell
# Deploy EVPN/VXLAN Fabric
$ ansible-playbook dc1-fabric-deploy-cvp.yml --tags build

TASK [eos_l3ls_evpn : Include device structured configuration, that was previously generated.] 
ok: [DC1-SPINE1 -> localhost]
ok: [DC1-SPINE2 -> localhost]
ok: [DC1-LEAF1A -> localhost]
ok: [DC1-LEAF1B -> localhost]
ok: [DC1-LEAF2A -> localhost]
ok: [DC1-LEAF2B -> localhost]

TASK [eos_l3ls_evpn : Generate EVPN fabric documentation in Markdown Format.] 
changed: [DC1-SPINE1 -> localhost]

TASK [eos_l3ls_evpn : Generate Leaf and Spine Point-To-Point Links summary in csv format.] 
changed: [DC1-SPINE1 -> localhost]

TASK [eos_l3ls_evpn : Generate Fabric Topology in csv format.] 
changed: [DC1-SPINE1 -> localhost]

TASK [eos_cli_config_gen : include device intended structure configuration variables] 
ok: [DC1-SPINE1 -> localhost]
ok: [DC1-SPINE2 -> localhost]
ok: [DC1-LEAF1A -> localhost]
ok: [DC1-LEAF1B -> localhost]
ok: [DC1-LEAF2A -> localhost]
ok: [DC1-LEAF2B -> localhost]

TASK [eos_cli_config_gen : Generate eos intended configuration] 
ok: [DC1-LEAF2A -> localhost]
ok: [DC1-SPINE1 -> localhost]
ok: [DC1-LEAF1A -> localhost]
ok: [DC1-LEAF2B -> localhost]
ok: [DC1-SPINE2 -> localhost]
ok: [DC1-LEAF1B -> localhost]

TASK [eos_cli_config_gen : Generate device documentation] 
changed: [DC1-SPINE1 -> localhost]
changed: [DC1-LEAF1A -> localhost]
changed: [DC1-LEAF2A -> localhost]
changed: [DC1-SPINE2 -> localhost]
changed: [DC1-LEAF1B -> localhost]
changed: [DC1-LEAF2B -> localhost]

PLAY [Configuration deployment with CVP] 

TASK [eos_config_deploy_cvp : generate intented variables] 
ok: [cv_server]

TASK [eos_config_deploy_cvp : Build DEVICES and CONTAINER definition for cv_server] 
changed: [cv_server -> localhost]

TASK [eos_config_deploy_cvp : Load CVP device information for cv_server] 
ok: [cv_server]

PLAY RECAP 
DC1-LEAF1A                 : ok=5    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
DC1-LEAF1B                 : ok=5    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
DC1-LEAF2A                 : ok=5    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
DC1-LEAF2B                 : ok=5    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
DC1-SPINE1                 : ok=8    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
DC1-SPINE2                 : ok=5    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
cv_server                  : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

#### Provision CloudVision Server

Use tag `provision` to deploy configuration to CloudVision and prepare devices to be updated:
- Create configlets on CloudVision servers
- Create containers on CloudVision using inventory structure
- Move devices to containers
- Attach configlets to devices.

This tag does not execute any pending tasks. It is a manual action that can be done with a Change Control. 
If you want to automatically deploy, just use `execute_tasks: True` in [__`eos_config_deploy_cvp`__](https://github.com/titom73/ansible-avd-cloudvision-demo/blob/9cbacf68ef91a5835a6e210017e9f00c8aa6037e/dc1-fabric-deploy-cvp.yml#L27) role.

```shell
# Deploy EVPN/VXLAN Fabric
$ ansible-playbook dc1-fabric-deploy-cvp.yml --tags provision
```

#### Execute Pending tasks using a change control

Go to _Provisioning > Change Control_ to create a new change control

![Change Control Example](data/figure-2-cloudvision-change-control.png)

This change control is an example and you are free to build structure you want. In this scenario, all tasks can be run in parallel as we just rollout an EVPN/VXLAN fabric.

## Analyze result.

Once devices rebooted, you can review fabric status on devices themselfs or on on CloudVision as well.

### Topology Update

Topology has been updated accordingly

![Lab Topology](data/cloudvision-device-topology.png)

### Configlet list

A set of new configlets have been configured on CloudVision and attached to devices

![Lab Topology](data/cloudvision-deployed-configlet.png)


### Check device status

To validate deployment, connect to devices and issue some commands:

__BGP Status__

```
DC1-LEAF1B#show bgp evpn summary 
BGP summary information for VRF default
Router identifier 192.168.255.4, local AS number 65101
Neighbor         V  AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State   PfxRcd PfxAcc
  192.168.255.1    4  65001             56        66    0    0 00:00:36 Estab   86     86
  192.168.255.2    4  65001             55        39    0    0 00:00:44 Estab   86     86
```

__VXLAN address table__

```
DC1-LEAF1B#show vxlan  address-table 
          Vxlan Mac Address Table
----------------------------------------------------------------------

VLAN  Mac Address     Type     Prt  VTEP             Moves   Last Move
----  -----------     ----     ---  ----             -----   ---------
1191  0e1d.c07f.d96c  EVPN     Vx1  192.168.254.5    1       0:00:04 ago
1192  0e1d.c07f.d96c  EVPN     Vx1  192.168.254.5    1       0:00:02 ago
1193  0e1d.c07f.d96c  EVPN     Vx1  192.168.254.5    1       0:00:04 ago
1194  0e1d.c07f.d96c  EVPN     Vx1  192.168.254.5    1       0:00:02 ago
1195  0e1d.c07f.d96c  EVPN     Vx1  192.168.254.5    1       0:00:02 ago
1196  0e1d.c07f.d96c  EVPN     Vx1  192.168.254.5    1       0:00:02 ago
1197  0e1d.c07f.d96c  EVPN     Vx1  192.168.254.5    1       0:00:04 ago
1198  0e1d.c07f.d96c  EVPN     Vx1  192.168.254.5    1       0:00:04 ago
1199  0e1d.c07f.d96c  EVPN     Vx1  192.168.254.5    1       0:00:02 ago
Total Remote Mac Addresses for this criterion: 9
```

### Check device connectivity

Connect on server 01 and issue a ping to server 02.

```shell
root@Server01:~# ping 10.1.10.12 -c 5
PING 10.1.10.12 (10.1.10.12) 56(84) bytes of data.
64 bytes from 10.1.10.12: icmp_seq=1 ttl=64 time=0.033 ms
64 bytes from 10.1.10.12: icmp_seq=2 ttl=64 time=0.026 ms
64 bytes from 10.1.10.12: icmp_seq=3 ttl=64 time=0.021 ms
64 bytes from 10.1.10.12: icmp_seq=4 ttl=64 time=0.026 ms
64 bytes from 10.1.10.12: icmp_seq=5 ttl=64 time=0.034 ms

--- 10.1.10.12 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 3998ms
rtt min/avg/max/mdev = 0.021/0.028/0.034/0.004 ms
```

## Revert topology

Once demo is over, you can revert to previous stage:

- Reset devices to ZTP mode (Only devices part of the demo)
- Remove configlet deployed previously
- Remove dedicated container topology
- Reboot devices

Playbook: [`dc1-fabric-reset-cvp.yml`](dc1-fabric-reset-cvp.yml)


```shell
# Reset EVPN/VXLAN Fabric tp ZTP
$ ansible-playbook dc1-fabric-reset-cvp.yml
```
