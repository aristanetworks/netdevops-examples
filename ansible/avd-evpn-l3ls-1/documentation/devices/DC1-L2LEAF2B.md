# DC1-L2LEAF2B

## Management Interfaces

### Management Interfaces Summary

IPv4

| Management Interface | description | VRF | IP Address | Gateway |
| -------------------- | ----------- | --- | ---------- | ------- |
| Management1 | oob_management | MGMT | 192.168.200.114/24 | 192.168.200.1 |

IPv6

| Management Interface | description | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | --- | ------------ | ------------ |
| Management1 | oob_management | MGMT | ||

### Management Interfaces Device Configuration

```eos
interface Management1
   description oob_management
   vrf MGMT
   ip address 192.168.200.114/24
!
```

## Hardware Counters

No Hardware Counters defined

## Aliases

alias copp show policy-map copp copp-system-policy
alias help bash echo -e "sib : show ip bgp\nsibs : show ip bgp summary\nsiib : show ip int brief\nsir : show ip route\nsenz : show interface counter error | nz\nsnz : show interface counter | nz\nsps : show port-channel summary\nspd : show port-channel detail all\nsqnz : show interface counter queue | nz\nsrnz : show interface counter rate | nz\nsmac : show mac address-table dynamic\nsarp : show ip arp\ncopp : show policy-map copp copp-system-policy\ninfo : version, serial and mlag"
alias sarp show ip arp
alias senz show interface counter error | nz
alias sib show ip bgp
alias sibs show ip bgp summary
alias siib show ip int brief
alias sir show ip route
alias smac show mac address-table dynamic
alias snz show interface counter | nz
alias spd show port-channel %1 detail all
alias sps show port-channel summary
alias sqnz show interface counter queue | nz
alias srnz show interface counter rate | nz
!
alias info
   10 bash SERIAL=$(FastCli -p 15 -c 'show version' | grep Serial | tr -s ' ' | cut -d ' ' -f 3 | tr -d '\r');echo -e "SN : $SERIAL"
   20 bash VERSION=$(FastCli -p 15 -c 'show version' | grep image | tr -s ' ' | cut -d ' ' -f 4 | tr -d '\r');echo -e "EOS VERSION : $VERSION"
   30 bash DOMAIN=$(FastCli -p 15 -c 'show mlag' | grep domain | tr -s ' ' | cut -d ' ' -f 3 | tr -d '\r');echo -e "MLAG DOMAIN : $DOMAIN"
   40 bash STATE=$(FastCli -p 15 -c 'show mlag' | grep state | tr -s ' ' | cut -d ' ' -f 3 | tr -d '\r');echo -e "MLAG STATE : $STATE"

!
## TerminAttr Daemon

### TerminAttr Daemon Summary

| CV Compression | Ingest gRPC URL | Ingest Authentication Key | Smash Excludes | Ingest Exclude | Ingest VRF |  NTP VRF |
| -------------- | --------------- | ------------------------- | -------------- | -------------- | ---------- | -------- |
| gzip | 192.168.200.11:9910 | telarista | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | MGMT | MGMT |

### TerminAttr Daemon Device Configuration

```eos
daemon TerminAttr
   exec /usr/bin/TerminAttr -ingestgrpcurl=192.168.200.11:9910 -cvcompression=gzip -ingestauth=key,telarista -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -ingestvrf=MGMT -taillogs
   no shutdown
!
```

## Internal VLAN allocation Policy

### Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

### Internal VLAN Allocation Policy Configuration

```eos
vlan internal order ascending range 1006 1199
!
```

## IP IGMP Snooping


## Logging

No logging settings defined

## Domain Lookup

DNS domain lookup not defined

## Name Servers

### Name Servers Summary

| Name Server | Source VRF |
| ----------- | ---------- |
| 192.168.200.5 | MGMT |
| 8.8.8.8 | MGMT |

### Name Servers Device Configuration

```eos
ip name-server vrf MGMT 192.168.200.5
ip name-server vrf MGMT 8.8.8.8
!
```

## DNS Domain

DNS domain not defined

## NTP

### NTP Summary

Local Interface: Management1

VRF: MGMT


| Node | Primary |
| ---- | ------- |
| 0.north-america.pool.ntp.org | true |
| 1.north-america.pool.ntp.org | - |

### NTP Device Configuration

```eos
ntp local-interface vrf MGMT Management1
ntp server vrf MGMT 0.north-america.pool.ntp.org prefer
ntp server vrf MGMT 1.north-america.pool.ntp.org
!
```

## Router L2 VPN

Router L2 VPN not defined

## SFlow

No sFlow defined

## Spanning Tree

### Spanning Tree Summary

Mode: mstp

**MSTP Instance and Priority**:

| Instance | Priority |
| -------- | -------- |
| 0 | 16384 |

### Spanning Tree Device Configuration

```eos
spanning-tree mode mstp
no spanning-tree vlan-id 4094
spanning-tree mst 0 priority 16384
!
```


TACACS Servers Not Configured


IP TACACS source interfaces not defined


AAA server groups not defined

## AAA Authentication

AAA authentication not defined

## AAA Authorization

AAA authorization not defined

## AAA Accounting

AAA accounting not defined

## Local Users

### Local Users Summary

| User | Privilege | role |
| ---- | --------- | ---- |
| admin | 15 | network-admin |
| cvpadmin | 15 | network-admin |

### Local Users Device Configuration

```eos
username admin privilege 15 role network-admin secret sha512 $6$Df86J4/SFMDE3/1K$Hef4KstdoxNDaami37cBquTWOTplC.miMPjXVgQxMe92.e5wxlnXOLlebgPj8Fz1KO0za/RCO7ZIs4Q6Eiq1g1
username cvpadmin privilege 15 role network-admin secret sha512 $6$rZKcbIZ7iWGAWTUM$TCgDn1KcavS0s.OV8lacMTUkxTByfzcGlFlYUWroxYuU7M/9bIodhRO7nXGzMweUxvbk8mJmQl8Bh44cRktUj.
!
```

## VLANs

### VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 110 | Tenant_A_OP_Zone_1 | none  |
| 111 | Tenant_A_OP_Zone_2 | none  |
| 120 | Tenant_A_WEB_Zone_1 | none  |
| 121 | Tenant_A_WEBZone_2 | none  |
| 130 | Tenant_A_APP_Zone_1 | none  |
| 131 | Tenant_A_APP_Zone_2 | none  |
| 140 | Tenant_A_DB_BZone_1 | none  |
| 141 | Tenant_A_DB_Zone_2 | none  |
| 160 | Tenant_A_VMOTION | none  |
| 161 | Tenant_A_NFS | none  |
| 210 | Tenant_B_OP_Zone_1 | none  |
| 211 | Tenant_B_OP_Zone_2 | none  |
| 310 | Tenant_C_OP_Zone_1 | none  |
| 311 | Tenant_C_OP_Zone_2 | none  |
| 4094 | MLAG_PEER | MLAG  |

### VLANs Device Configuration

```eos
vlan 110
   name Tenant_A_OP_Zone_1
!
vlan 111
   name Tenant_A_OP_Zone_2
!
vlan 120
   name Tenant_A_WEB_Zone_1
!
vlan 121
   name Tenant_A_WEBZone_2
!
vlan 130
   name Tenant_A_APP_Zone_1
!
vlan 131
   name Tenant_A_APP_Zone_2
!
vlan 140
   name Tenant_A_DB_BZone_1
!
vlan 141
   name Tenant_A_DB_Zone_2
!
vlan 160
   name Tenant_A_VMOTION
!
vlan 161
   name Tenant_A_NFS
!
vlan 210
   name Tenant_B_OP_Zone_1
!
vlan 211
   name Tenant_B_OP_Zone_2
!
vlan 310
   name Tenant_C_OP_Zone_1
!
vlan 311
   name Tenant_C_OP_Zone_2
!
vlan 4094
   name MLAG_PEER
   trunk group MLAG
!
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT |  disabled |

### VRF Instances Device Configuration

```eos
vrf instance MGMT
!
```

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

| Interface | Description | MTU | Type | Mode | Allowed VLANs (trunk) | Trunk Group | MLAG ID | VRF | IP Address | IPv6 Address |
| --------- | ----------- | --- | ---- | ---- | --------------------- | ----------- | ------- | --- | ---------- | ------------ |
| Port-Channel1 | DC1-SVC3B_Po7 | 1500 | switched | trunk | 110-111,120-121,130-131,140-141,160-161,210-211,310-311 | - | 1 | - | - | - |
| Port-Channel3 | MLAG_PEER_DC1-L2LEAF2A_Po3 | 1500 | switched | trunk | 2-4094 | MLAG | - | - | - | - |

### Port-Channel Interfaces Device Configuration

```eos
interface Port-Channel1
   description DC1-SVC3B_Po7
   switchport trunk allowed vlan 110-111,120-121,130-131,140-141,160-161,210-211,310-311
   switchport mode trunk
   mlag 1
!
interface Port-Channel3
   description MLAG_PEER_DC1-L2LEAF2A_Po3
   switchport trunk allowed vlan 2-4094
   switchport mode trunk
   switchport trunk group MLAG
!
```

## Ethernet Interfaces

### Ethernet Interfaces Summary

| Interface | Description | MTU | Type | Mode | Allowed VLANs (Trunk) | Trunk Group | VRF | IP Address | Channel-Group ID | Channel-Group Type |
| --------- | ----------- | --- | ---- | ---- | --------------------- | ----------- | --- | ---------- | ---------------- | ------------------ |
| Ethernet1 | DC1-SVC3A_Ethernet8 | *1500 | *switched | *trunk | *110-111,120-121,130-131,140-141,160-161,210-211,310-311 | - | - | - | 1 | active |
| Ethernet2 | DC1-SVC3B_Ethernet8 | *1500 | *switched | *trunk | *110-111,120-121,130-131,140-141,160-161,210-211,310-311 | - | - | - | 1 | active |
| Ethernet3 | MLAG_PEER_DC1-L2LEAF2A_Ethernet3 | *1500 | *switched | *trunk | *2-4094 | *MLAG | - | - | 3 | active |
| Ethernet4 | MLAG_PEER_DC1-L2LEAF2A_Ethernet4 | *1500 | *switched | *trunk | *2-4094 | *MLAG | - | - | 3 | active |

*Inherited from Port-Channel Interface

### Ethernet Interfaces Device Configuration

```eos
interface Ethernet1
   description DC1-SVC3A_Ethernet8
   channel-group 1 mode active
!
interface Ethernet2
   description DC1-SVC3B_Ethernet8
   channel-group 1 mode active
!
interface Ethernet3
   description MLAG_PEER_DC1-L2LEAF2A_Ethernet3
   channel-group 3 mode active
!
interface Ethernet4
   description MLAG_PEER_DC1-L2LEAF2A_Ethernet4
   channel-group 3 mode active
!
```

## Loopback Interfaces

No Loopback interfaces defined

## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF | IP Address | IP Address Virtual | IP Router Virtual Address (vARP) |
| --------- | ----------- | --- | ---------- | ------------------ | -------------------------------- |
| Vlan4094 | MLAG_PEER | Global Routing Table | 10.255.252.17/31 | - | - |

### VLAN Interfaces Device Configuration

```eos
interface Vlan4094
   description MLAG_PEER
   no autostate
   ip address 10.255.252.17/31
!
```

## VXLAN Interface

No VXLAN interface defined

## Virtual Router MAC Address & Virtual Source NAT


## IPv6 Extended Access-lists

IPv6 Extended Access-lists not defined

## IPv6 Standard Access-lists

IPv6 Standard Access-lists not defined

## Extended Access-lists

Extended Access-lists not defined

## Standard Access-lists

Standard Access-lists not defined

## Static Routes

### Static Routes Summary

| VRF | Destination Prefix | Fowarding Address / Interface |
| --- | ------------------ | ----------------------------- |
| MGMT | 0.0.0.0/0 | 192.168.200.1 |

### Static Routes Device Configuration

```eos
ip route vrf MGMT 0.0.0.0/0 192.168.200.1
!
```

## Event Handler

No Event Handler Defined

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| MGMT | False |

### IP Routing Device Configuration

```eos
ip routing
no ip routing vrf MGMT
!
```

## Prefix Lists

Prefix lists not defined

## IPv6 Prefix Lists

IPv6 Prefix lists not defined

## IPv6 Routing

### IPv6 Routing Summary

| VRF | IPv6 Routing Enabled |
| --- | -------------------- |
| MGMT | False |

### IPv6 Routing Device Configuration

```eos
```

## MLAG

### MLAG Summary

| domain-id | local-interface | peer-address | peer-link |
| --------- | --------------- | ------------ | --------- |
| DC1_L2LEAF2 | Vlan4094 | 10.255.252.16 | Port-Channel3 |

Dual primary detection is enabled. The detection delay is 5 seconds.

### MLAG Device Configuration

```eos
mlag configuration
   domain-id DC1_L2LEAF2
   local-interface Vlan4094
   peer-address 10.255.252.16
   peer-address heartbeat 192.168.200.113 vrf MGMT
   peer-link Port-Channel3
   dual-primary detection delay 5 action errdisable all-interfaces
   reload-delay mlag 300
   reload-delay non-mlag 330
!
```

## Route Maps

No route maps defined

## Peer Filters

No Peer Filters defined

## Router BFD

### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 1200 | 1200 | 3 |

### Router BFD Multihop Device Configuration

```eos
router bfd
   multihop interval 1200 min-rx 1200 multiplier 3
!
```

## Router BGP

Router BGP not defined

## Router Multicast

Routing multicast not defined

## Router PIM Sparse Mode

Router PIM sparse mode not defined

## VM Tracer Sessions

No VM tracer session defined

## Management Security

Management Security not defined

## Platform

No Platform parameters defined
