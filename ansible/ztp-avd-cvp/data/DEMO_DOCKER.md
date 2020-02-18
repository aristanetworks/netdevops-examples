
# Demo script

This demo script uses a docker images to streamline dependencies and make it easier to run on any system.

## Build local docker image

A local image needs to be generated locally before running any other commands:

```shell
$ make build
docker build -f Dockerfile -t arista/avd-cvp-demo:latest .
Sending build context to Docker daemon  6.855MB
Step 1/12 : FROM python:3-alpine3.6
 ---> 37daba746bbe
Step 2/12 : LABEL maintainer="Arista Ansible Team <ansible@arista.com>"
...
```

## Power up devices.

Power up your devices what ever the solution is. You will see them in the __`undefined`__ container

![ZTP Registration](../data/cloudvision-ztpd-devices.png)

__Check there is no container__

![Streaming Inventory](../data/streaming-inventory.png)


__Check Configlets are not present__

![Configlets](../data/cloudvision-initial-configlet.png)


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

### Run Playbook

```shell
# Deploy EVPN/VXLAN Fabric
$make deploy
docker run -it --rm -v $(PWD):/project $(DOCKER_NAME):latest ansible-playbook ansible-playbook dc1-fabric-deploy-cvp.yml

PLAY [Build Switch configuration] **********

TASK [eos-l3ls-evpn : Generate switch configuration in structured format (yaml)] **********
ok: [DC1-LEAF1B -> localhost]
ok: [DC1-SPINE2 -> localhost]
ok: [DC1-LEAF1A -> localhost]
ok: [DC1-LEAF2A -> localhost]
ok: [DC1-LEAF2B -> localhost]
ok: [DC1-SPINE1 -> localhost]

TASK [eos-l3ls-evpn : include device structured configuration] **********
ok: [DC1-SPINE1 -> localhost]
ok: [DC1-SPINE2 -> localhost]
ok: [DC1-LEAF1A -> localhost]
ok: [DC1-LEAF1B -> localhost]
ok: [DC1-LEAF2A -> localhost]
ok: [DC1-LEAF2B -> localhost]

TASK [eos-l3ls-evpn : Generate EVPN fabric documentation] **********
ok: [DC1-SPINE1 -> localhost]

TASK [eos-l3ls-evpn : Generate EVPN fabric documentation - p2p links csv] **********
ok: [DC1-SPINE1 -> localhost]

TASK [eos-cli-config-gen : include data center fabric variables] **********
ok: [DC1-SPINE1 -> localhost]
ok: [DC1-SPINE2 -> localhost]
ok: [DC1-LEAF1A -> localhost]
ok: [DC1-LEAF1B -> localhost]
ok: [DC1-LEAF2A -> localhost]
ok: [DC1-LEAF2B -> localhost]

TASK [eos-cli-config-gen : Generate eos intended configuration] **********
ok: [DC1-SPINE1 -> localhost]
ok: [DC1-LEAF1B -> localhost]
ok: [DC1-LEAF2A -> localhost]
ok: [DC1-LEAF1A -> localhost]
ok: [DC1-SPINE2 -> localhost]
ok: [DC1-LEAF2B -> localhost]

TASK [eos-l3ls-evpn : Generate EVPN fabric documentation] **********
ok: [DC1-SPINE1 -> localhost]

TASK [eos-l3ls-evpn : Generate EVPN fabric documentation - p2p links csv] **********
ok: [DC1-SPINE1 -> localhost]

TASK [eos-cli-config-gen : include data center fabric variables] **********
ok: [DC1-SPINE1 -> localhost]
ok: [DC1-SPINE2 -> localhost]
ok: [DC1-LEAF1A -> localhost]
ok: [DC1-LEAF1B -> localhost]
ok: [DC1-LEAF2A -> localhost]
ok: [DC1-LEAF2B -> localhost]

TASK [eos-cli-config-gen : Generate eos intended configuration] **********
ok: [DC1-SPINE2 -> localhost]
ok: [DC1-LEAF1A -> localhost]
ok: [DC1-LEAF2A -> localhost]
ok: [DC1-LEAF1B -> localhost]
ok: [DC1-LEAF2B -> localhost]
ok: [DC1-SPINE1 -> localhost]

TASK [eos-cli-config-gen : Generate device documentation] **********
ok: [DC1-SPINE1 -> localhost]
ok: [DC1-LEAF1B -> localhost]
ok: [DC1-SPINE2 -> localhost]
ok: [DC1-LEAF2A -> localhost]
ok: [DC1-LEAF2B -> localhost]
ok: [DC1-LEAF1A -> localhost]

PLAY [Configuration deployment with CVP] **********

TASK [eos-config-deploy-cvp : generate intented variables] **********
ok: [cvp]

TASK [eos-config-deploy-cvp : Build DEVICES and CONTAINER definition for cvp] **********
ok: [cvp -> localhost]

TASK [eos-config-deploy-cvp : Load CVP device information for cvp] **********
ok: [cvp]

TASK [eos-config-deploy-cvp : Collecting facts from CVP cvp.] **********
ok: [cvp]

TASK [eos-config-deploy-cvp : Create configlets on CVP cvp.] **********
changed: [cvp]

TASK [eos-config-deploy-cvp : Building Container topology on cvp] **********
changed: [cvp]

TASK [eos-config-deploy-cvp : Configure devices on cvp] **********
changed: [cvp]

TASK [eos-config-deploy-cvp : Execute pending tasks on cvp] **********
changed: [cvp]

PLAY RECAP **********
DC1-LEAF1A                 : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
DC1-LEAF1B                 : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
DC1-LEAF2A                 : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
DC1-LEAF2B                 : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
DC1-SPINE1                 : ok=7    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
DC1-SPINE2                 : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
cvp                        : ok=8    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Analyze result.

Once devices rebooted, you can review fabric status on devices themselfs or on on CloudVision as well.

### Topology Update

Topology has been updated accordingly

![Lab Topology](../data/cloudvision-device-topology.png)

### Configlet list

A set of new configlets have been configured on CloudVision and attached to devices

![Lab Topology](../data/cloudvision-deployed-configlet.png)


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
$ make reset
docker run -it --rm -v $(PWD):/project $(DOCKER_NAME):latest ansible-playbook ansible-playbook dc1-fabric-reset-cvp.yml
```