# DC-LEAF1 Commands Output

## Table of Contents

- [show lldp neighbors](#show-lldp-neighbors)
- [show ip interface brief](#show-ip-interface-brief)
- [show interfaces description](#show-interfaces-description)
- [show version](#show-version)
- [show running-config](#show-running-config)
## show interfaces description

```
Interface                      Status         Protocol           Description
Et1                            up             up                 P2P_LINK_TO_DC-SPINE1_Ethernet1
Et2                            up             up                 P2P_LINK_TO_DC-SPINE2_Ethernet1
Et3                            up             up                 
Et4                            up             up                 
Et5                            up             up                 server01_E1
Et6                            up             up                 server02_E1
Et7                            up             up                 server03_E1
Et8                            up             up                 
Et9                            up             up                 
Et10                           up             up                 
Et11                           up             up                 
Lo0                            up             up                 EVPN_Overlay_Peering
Lo1                            up             up                 VTEP_VXLAN_Tunnel_Source
Lo100                          up             up                 Tenant_blue_vrf_VTEP_DIAGNOSTICS
Lo200                          up             up                 Tenant_green_vrf_VTEP_DIAGNOSTICS
Ma1                            up             up                 oob_management
Po5                            up             up                 server01_PortChannel
Po6                            up             up                 server02_PortChannel
Po7                            up             up                 server03_PortChannel
Vl10                           up             up                 Tenant_blue_compute
Vl20                           up             up                 Tenant_green_compute
Vl30                           up             up                 Tenant_green_storage
Vl1197                         up             up                 
Vl1198                         up             up                 
Vl1199                         up             up                 
Vx1                            up             up
```
## show ip interface brief

```
Address 
Interface       IP Address           Status     Protocol         MTU    Owner   
--------------- -------------------- ---------- ------------ ---------- ------- 
Ethernet1       10.10.100.1/31       up         up              1500            
Ethernet2       10.10.100.3/31       up         up              1500            
Loopback0       192.168.100.3/32     up         up             65535            
Loopback1       192.168.101.3/32     up         up             65535            
Loopback100     10.255.1.3/32        up         up             65535            
Loopback200     10.255.2.3/32        up         up             65535            
Management1     172.30.30.213/24     up         up              1500            
Vlan10          10.10.10.1/24        up         up              1500            
Vlan20          10.10.20.1/24        up         up              1500            
Vlan30          10.10.30.1/24        up         up              1500            
Vlan1197        unassigned           up         up              9164            
Vlan1198        unassigned           up         up              9164            
Vlan1199        unassigned           up         up              9164
```
## show lldp neighbors

```
Last table change time   : 0:27:31 ago
Number of table inserts  : 6
Number of table deletes  : 0
Number of table drops    : 0
Number of table age-outs : 0

Port          Neighbor Device ID         Neighbor Port ID    TTL 
---------- -------------------------- ---------------------- --- 
Et1           DC-SPINE1.homelab.io       Ethernet1           120 
Et2           DC-SPINE2.homelab.io       Ethernet1           120 
Et5           server01                   Ethernet1           120 
Et6           server02                   Ethernet1           120 
Et7           server03                   Ethernet1           120 
Ma1           mgmt-sw                    Ethernet9           120
```
## show running-config

```
! Command: show running-config
! device: DC-LEAF1 (vEOS, EOS-4.25.5M)
!
! boot system flash:/vEOS-lab.swi
!
no aaa root
!
username admin privilege 15 role network-admin secret sha512 $6$LJcUms0WZ9UyskIF$b6jUZMJmruk95uA0GPood4z4Tgb2aHKqnRhm7HyHl3kjsgE6mA5.V3W/vwl16WeICFvWWz1vkU1zQET0CbILG0
username cvpadmin privilege 15 role network-admin secret sha512 $6$pWE0vYbIJTmV0ZWc$nIrbLNYS3pIgpFj9vuzkchwyA19betlJZjWR.KE95GHwOALliiUUAu92JUWg9jQ12Yd3.aTQmWf.gRe2VNo2Y.
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -ingestgrpcurl=172.30.30.252:9910 -cvcompression=gzip -ingestauth=key,arista -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -ingestvrf=mgmt -taillogs
   no shutdown
!
vlan internal order ascending range 1006 1199
!
transceiver qsfp default-mode 4x10G
!
service routing protocols model multi-agent
!
hostname DC-LEAF1
ip name-server vrf mgmt 1.1.1.1
ip name-server vrf mgmt 172.30.30.6
dns domain homelab.io
!
ntp local-interface vrf mgmt Management1
ntp server vrf mgmt time.google.com prefer iburst
!
spanning-tree mode mstp
spanning-tree mst 0 priority 4096
!
clock timezone America/Toronto
!
vlan 10
   name Tenant_blue_compute
!
vlan 20
   name Tenant_green_compute
!
vlan 30
   name Tenant_green_storage
!
vrf instance Tenant_blue_vrf
!
vrf instance Tenant_green_vrf
!
vrf instance mgmt
!
interface Port-Channel5
   description server01_PortChannel
   switchport trunk allowed vlan 10
   switchport mode trunk
   !
   evpn ethernet-segment
      identifier 0000:0000:0001:1010:1010
      route-target import 00:01:10:10:10:10
   lacp system-id 0001.1010.1010
!
interface Port-Channel6
   description server02_PortChannel
   switchport trunk allowed vlan 20
   switchport mode trunk
   !
   evpn ethernet-segment
      identifier 0000:0000:0002:2020:2020
      route-target import 00:02:20:20:20:20
   lacp system-id 0002.2020.2020
!
interface Port-Channel7
   description server03_PortChannel
   switchport trunk allowed vlan 30
   switchport mode trunk
   !
   evpn ethernet-segment
      identifier 0000:0000:0003:3030:3030
      route-target import 00:03:30:30:30:30
   lacp system-id 0003.3030.3030
!
interface Ethernet1
   description P2P_LINK_TO_DC-SPINE1_Ethernet1
   no switchport
   ip address 10.10.100.1/31
!
interface Ethernet2
   description P2P_LINK_TO_DC-SPINE2_Ethernet1
   no switchport
   ip address 10.10.100.3/31
!
interface Ethernet3
!
interface Ethernet4
!
interface Ethernet5
   description server01_E1
   channel-group 5 mode active
!
interface Ethernet6
   description server02_E1
   channel-group 6 mode active
!
interface Ethernet7
   description server03_E1
   channel-group 7 mode active
!
interface Ethernet8
!
interface Ethernet9
!
interface Ethernet10
!
interface Ethernet11
!
interface Loopback0
   description EVPN_Overlay_Peering
   ip address 192.168.100.3/32
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   ip address 192.168.101.3/32
!
interface Loopback100
   description Tenant_blue_vrf_VTEP_DIAGNOSTICS
   vrf Tenant_blue_vrf
   ip address 10.255.1.3/32
!
interface Loopback200
   description Tenant_green_vrf_VTEP_DIAGNOSTICS
   vrf Tenant_green_vrf
   ip address 10.255.2.3/32
!
interface Management1
   description oob_management
   vrf mgmt
   ip address 172.30.30.213/24
!
interface Vlan10
   description Tenant_blue_compute
   vrf Tenant_blue_vrf
   ip address virtual 10.10.10.1/24
!
interface Vlan20
   description Tenant_green_compute
   vrf Tenant_green_vrf
   ip address virtual 10.10.20.1/24
!
interface Vlan30
   description Tenant_green_storage
   vrf Tenant_green_vrf
   ip address virtual 10.10.30.1/24
!
interface Vxlan1
   vxlan source-interface Loopback1
   vxlan udp-port 4789
   vxlan vlan 10 vni 10010
   vxlan vlan 20 vni 20020
   vxlan vlan 30 vni 20030
   vxlan vrf Tenant_blue_vrf vni 100
   vxlan vrf Tenant_green_vrf vni 200
!
ip virtual-router mac-address 00:1c:73:00:dc:01
ip address virtual source-nat vrf Tenant_blue_vrf address 10.255.1.3
ip address virtual source-nat vrf Tenant_green_vrf address 10.255.2.3
!
ip routing
ip routing vrf Tenant_blue_vrf
ip routing vrf Tenant_green_vrf
no ip routing vrf mgmt
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 192.168.100.0/24 eq 32
   seq 20 permit 192.168.101.0/24 eq 32
!
ip route vrf mgmt 0.0.0.0/0 172.30.30.1
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
!
router bfd
   multihop interval 1200 min-rx 1200 multiplier 3
!
router bgp 65101
   router-id 192.168.100.3
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
   neighbor 10.10.100.0 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.10.100.0 description DC-SPINE1_Ethernet1
   neighbor 10.10.100.2 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.10.100.2 description DC-SPINE2_Ethernet1
   neighbor 192.168.100.1 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.100.1 remote-as 65100
   neighbor 192.168.100.1 description DC-SPINE1
   neighbor 192.168.100.2 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.100.2 remote-as 65100
   neighbor 192.168.100.2 description DC-SPINE2
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan 10
      rd 192.168.100.3:10010
      route-target both 10010:10010
      redistribute learned
   !
   vlan 20
      rd 192.168.100.3:20020
      route-target both 20020:20020
      redistribute learned
   !
   vlan 30
      rd 192.168.100.3:20030
      route-target both 20030:20030
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
      rd 192.168.100.3:100
      route-target import evpn 100:100
      route-target export evpn 100:100
      router-id 192.168.100.3
      redistribute connected
   !
   vrf Tenant_green_vrf
      rd 192.168.100.3:200
      route-target import evpn 200:200
      route-target export evpn 200:200
      router-id 192.168.100.3
      redistribute connected
!
management api http-commands
   no shutdown
   !
   vrf mgmt
      no shutdown
!
end
```
## show version

```
vEOS
Hardware version: 
Serial number: 
Hardware MAC address: 5001.33b3.10b4
System MAC address: 5001.33b3.10b4

Software image version: 4.25.5M
Architecture: i686
Internal build version: 4.25.5M-23663359.4255M
Internal build ID: 60baa7f9-12cb-41d2-ad7d-b6b2fcccfa92

Uptime: 0 weeks, 0 days, 0 hours and 30 minutes
Total memory: 2006880 kB
Free memory: 1078448 kB
```
