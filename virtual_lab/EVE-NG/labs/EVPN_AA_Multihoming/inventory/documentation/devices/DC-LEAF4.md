# DC-LEAF4
# Table of Contents
<!-- toc -->

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [DNS Domain](#dns-domain)
  - [Name Servers](#name-servers)
  - [NTP](#ntp)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Configuration](#internal-vlan-allocation-policy-configuration)
- [VLANs](#vlans)
  - [VLANs Summary](#vlans-summary)
  - [VLANs Device Configuration](#vlans-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [ACL](#acl)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Virtual Source NAT](#virtual-source-nat)
  - [Virtual Source NAT Summary](#virtual-source-nat-summary)
  - [Virtual Source NAT Configuration](#virtual-source-nat-configuration)
- [Quality Of Service](#quality-of-service)

<!-- toc -->
# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | mgmt | 172.30.30.216/24 | 172.30.30.1 |

#### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | mgmt | -  | - |

### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   no shutdown
   vrf mgmt
   ip address 172.30.30.216/24
```

## DNS Domain

### DNS domain: homelab.io

### DNS Domain Device Configuration

```eos
!
dns domain homelab.io
!
```

## Name Servers

### Name Servers Summary

| Name Server | Source VRF |
| ----------- | ---------- |
| 172.30.30.6 | mgmt |
| 1.1.1.1 | mgmt |

### Name Servers Device Configuration

```eos
ip name-server vrf mgmt 1.1.1.1
ip name-server vrf mgmt 172.30.30.6
```

## NTP

### NTP Summary

- Local Interface: Management1

- VRF: mgmt

| Node | Primary |
| ---- | ------- |
| time.google.com iburst | true |

### NTP Device Configuration

```eos
!
ntp local-interface vrf mgmt Management1
ntp server vrf mgmt time.google.com iburst prefer
```

## Management API HTTP

### Management API HTTP Summary

| HTTP | HTTPS |
| ---------- | ---------- |
| default | true |

### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| mgmt | - | - |


### Management API HTTP Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf mgmt
      no shutdown
```

# Authentication

## Local Users

### Local Users Summary

| User | Privilege | Role |
| ---- | --------- | ---- |
| admin | 15 | network-admin |
| cvpadmin | 15 | network-admin |

### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin secret sha512 $6$LJcUms0WZ9UyskIF$b6jUZMJmruk95uA0GPood4z4Tgb2aHKqnRhm7HyHl3kjsgE6mA5.V3W/vwl16WeICFvWWz1vkU1zQET0CbILG0
username cvpadmin privilege 15 role network-admin secret sha512 $6$pWE0vYbIJTmV0ZWc$nIrbLNYS3pIgpFj9vuzkchwyA19betlJZjWR.KE95GHwOALliiUUAu92JUWg9jQ12Yd3.aTQmWf.gRe2VNo2Y.
```

# Monitoring

## TerminAttr Daemon

### TerminAttr Daemon Summary

| CV Compression | Ingest gRPC URL | Ingest Authentication Key | Smash Excludes | Ingest Exclude | Ingest VRF |  NTP VRF | AAA Disabled |
| -------------- | --------------- | ------------------------- | -------------- | -------------- | ---------- | -------- | ------ |
| gzip | 172.30.30.252:9910 | arista | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | mgmt | mgmt | False |

### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -ingestgrpcurl=172.30.30.252:9910 -cvcompression=gzip -ingestauth=key,arista -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -ingestvrf=mgmt -taillogs
   no shutdown
```

# Spanning Tree

## Spanning Tree Summary

STP mode: **mstp**

### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 4096 |

### Global Spanning-Tree Settings


## Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
spanning-tree mst 0 priority 4096
```

# Internal VLAN Allocation Policy

## Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

## Internal VLAN Allocation Policy Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

# VLANs

## VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 40 | Tenant_red_storage | none  |
| 50 | Tenant_blue_storage | none  |

## VLANs Device Configuration

```eos
!
vlan 40
   name Tenant_red_storage
!
vlan 50
   name Tenant_blue_storage
```

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet5 | server05_E2 | *trunk | *40 | *- | *- | 5 |
| Ethernet6 | server06_E2 | *trunk | *50 | *- | *- | 6 |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_LINK_TO_DC-SPINE1_Ethernet4 | routed | - | 10.10.100.13/31 | default | 1500 | false | - | - |
| Ethernet2 | P2P_LINK_TO_DC-SPINE2_Ethernet4 | routed | - | 10.10.100.15/31 | default | 1500 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_DC-SPINE1_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 10.10.100.13/31
!
interface Ethernet2
   description P2P_LINK_TO_DC-SPINE2_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 10.10.100.15/31
!
interface Ethernet5
   description server05_E2
   no shutdown
   channel-group 5 mode active
!
interface Ethernet6
   description server06_E2
   no shutdown
   channel-group 6 mode active
```

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

#### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel5 | server05_PortChannel | switched | trunk | 40 | - | - | - | - | - | 0000:0000:0004:4040:4040 |
| Port-Channel6 | server06_PortChannel | switched | trunk | 50 | - | - | - | - | - | 0000:0000:0005:5050:5050 |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel5
   description server05_PortChannel
   no shutdown
   switchport
   switchport trunk allowed vlan 40
   switchport mode trunk
   evpn ethernet-segment
      identifier 0000:0000:0004:4040:4040
      route-target import 00:04:40:40:40:40
   lacp system-id 0004.4040.4040
!
interface Port-Channel6
   description server06_PortChannel
   no shutdown
   switchport
   switchport trunk allowed vlan 50
   switchport mode trunk
   evpn ethernet-segment
      identifier 0000:0000:0005:5050:5050
      route-target import 00:05:50:50:50:50
   lacp system-id 0005.5050.5050
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 192.168.100.6/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 192.168.101.6/32 |
| Loopback100 | Tenant_blue_vrf_VTEP_DIAGNOSTICS | Tenant_blue_vrf | 10.255.1.6/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |
| Loopback100 | Tenant_blue_vrf_VTEP_DIAGNOSTICS | Tenant_blue_vrf | - |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 192.168.100.6/32
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   no shutdown
   ip address 192.168.101.6/32
!
interface Loopback100
   description Tenant_blue_vrf_VTEP_DIAGNOSTICS
   no shutdown
   vrf Tenant_blue_vrf
   ip address 10.255.1.6/32
```

## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan40 |  Tenant_red_storage  |  Tenant_red_vrf  |  -  |  false  |
| Vlan50 |  Tenant_blue_storage  |  Tenant_blue_vrf  |  -  |  false  |

#### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan40 |  Tenant_red_vrf  |  -  |  10.10.40.1/24  |  -  |  -  |  -  |  -  |
| Vlan50 |  Tenant_blue_vrf  |  -  |  10.10.50.1/24  |  -  |  -  |  -  |  -  |


### VLAN Interfaces Device Configuration

```eos
!
interface Vlan40
   description Tenant_red_storage
   no shutdown
   vrf Tenant_red_vrf
   ip address virtual 10.10.40.1/24
!
interface Vlan50
   description Tenant_blue_storage
   no shutdown
   vrf Tenant_blue_vrf
   ip address virtual 10.10.50.1/24
```

## VXLAN Interface

### VXLAN Interface Summary

#### Source Interface: Loopback1

#### UDP port: 4789

#### VLAN to VNI Mappings

| VLAN | VNI |
| ---- | --- |
| 40 | 30040 |
| 50 | 10050 |

#### VRF to VNI Mappings

| VLAN | VNI |
| ---- | --- |
| Tenant_blue_vrf | 100 |
| Tenant_red_vrf | 300 |

### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   vxlan source-interface Loopback1
   vxlan udp-port 4789
   vxlan vlan 40 vni 30040
   vxlan vlan 50 vni 10050
   vxlan vrf Tenant_blue_vrf vni 100
   vxlan vrf Tenant_red_vrf vni 300
```

# Routing
## Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

## Virtual Router MAC Address

### Virtual Router MAC Address Summary

#### Virtual Router MAC Address: 00:1c:73:00:dc:01

### Virtual Router MAC Address Configuration

```eos
!
ip virtual-router mac-address 00:1c:73:00:dc:01
```

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | true|| mgmt | false |
| Tenant_blue_vrf | true |
| Tenant_red_vrf | true |

### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf mgmt
ip routing vrf Tenant_blue_vrf
ip routing vrf Tenant_red_vrf
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false || mgmt | false |
| Tenant_blue_vrf | false |
| Tenant_red_vrf | false |


## Static Routes

### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| mgmt  | 0.0.0.0/0 |  172.30.30.1  |  -  |  1  |  -  |  -  |  - |

### Static Routes Device Configuration

```eos
!
ip route vrf mgmt 0.0.0.0/0 172.30.30.1
```

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65104|  192.168.100.6 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 4 ecmp 4 |

### Router BGP Peer Groups

#### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Source | Loopback0 |
| Bfd | true |
| Ebgp multihop | 3 |
| Send community | all |
| Maximum routes | 0 (no limit) |

#### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65100 |
| Send community | all |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS | VRF |
| -------- | --------- | --- |
| 10.10.100.12 | Inherited from peer group IPv4-UNDERLAY-PEERS | default |
| 10.10.100.14 | Inherited from peer group IPv4-UNDERLAY-PEERS | default |
| 192.168.100.1 | 65100 | default |
| 192.168.100.2 | 65100 | default |

### Router BGP EVPN Address Family

#### Router BGP EVPN MAC-VRFs

##### VLAN Based

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 40 | 192.168.100.6:30040 | 30040:30040 | - | - | learned |
| 50 | 192.168.100.6:10050 | 10050:10050 | - | - | learned |

#### Router BGP EVPN VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Tenant_blue_vrf | 192.168.100.6:100 | connected |
| Tenant_red_vrf | 192.168.100.6:300 | connected |

### Router BGP Device Configuration

```eos
!
router bgp 65104
   router-id 192.168.100.6
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS password 7 q+VNViP5i4rVjW1cxFv2wA==
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS remote-as 65100
   neighbor IPv4-UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 10.10.100.12 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.10.100.12 description DC-SPINE1_Ethernet4
   neighbor 10.10.100.14 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.10.100.14 description DC-SPINE2_Ethernet4
   neighbor 192.168.100.1 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.100.1 remote-as 65100
   neighbor 192.168.100.1 description DC-SPINE1
   neighbor 192.168.100.2 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.100.2 remote-as 65100
   neighbor 192.168.100.2 description DC-SPINE2
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan 40
      rd 192.168.100.6:30040
      route-target both 30040:30040
      redistribute learned
   !
   vlan 50
      rd 192.168.100.6:10050
      route-target both 10050:10050
      redistribute learned
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
   !
   vrf Tenant_blue_vrf
      rd 192.168.100.6:100
      route-target import evpn 100:100
      route-target export evpn 100:100
      router-id 192.168.100.6
      redistribute connected
   !
   vrf Tenant_red_vrf
      rd 192.168.100.6:300
      route-target import evpn 300:300
      route-target export evpn 300:300
      router-id 192.168.100.6
      redistribute connected
```

# BFD

## Router BFD

### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 1200 | 1200 | 3 |

### Router BFD Multihop Device Configuration

```eos
!
router bfd
   multihop interval 1200 min-rx 1200 multiplier 3
```

# Multicast

## IP IGMP Snooping

### IP IGMP Snooping Summary

IGMP snooping is globally enabled.


### IP IGMP Snooping Device Configuration

```eos
```

# Filters

## Prefix-lists

### Prefix-lists Summary

#### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 192.168.100.0/24 eq 32 |
| 20 | permit 192.168.101.0/24 eq 32 |

### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 192.168.100.0/24 eq 32
   seq 20 permit 192.168.101.0/24 eq 32
```

## Route-maps

### Route-maps Summary

#### RM-CONN-2-BGP

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY |

### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
```

# ACL

# VRF Instances

## VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| mgmt | disabled |
| Tenant_blue_vrf | enabled |
| Tenant_red_vrf | enabled |

## VRF Instances Device Configuration

```eos
!
vrf instance mgmt
!
vrf instance Tenant_blue_vrf
!
vrf instance Tenant_red_vrf
```

# Virtual Source NAT

## Virtual Source NAT Summary

| Source NAT VRF | Source NAT IP Address |
| -------------- | --------------------- |
| Tenant_blue_vrf | 10.255.1.6 |

## Virtual Source NAT Configuration

```eos
!
ip address virtual source-nat vrf Tenant_blue_vrf address 10.255.1.6
```

# Quality Of Service
