# DC-SPINE2 Commands Output

## Table of Contents

- [show lldp neighbors](#show-lldp-neighbors)
- [show ip interface brief](#show-ip-interface-brief)
- [show interfaces description](#show-interfaces-description)
- [show version](#show-version)
- [show running-config](#show-running-config)
## show interfaces description

```
Interface                      Status         Protocol           Description
Et1                            up             up                 P2P_LINK_TO_DC-LEAF1_Ethernet2
Et2                            up             up                 P2P_LINK_TO_DC-LEAF2_Ethernet2
Et3                            up             up                 P2P_LINK_TO_DC-LEAF3_Ethernet2
Et4                            up             up                 P2P_LINK_TO_DC-LEAF4_Ethernet2
Et5                            up             up                 
Et6                            up             up                 
Et7                            up             up                 
Et8                            up             up                 
Et9                            up             up                 
Et10                           up             up                 
Et11                           up             up                 
Lo0                            up             up                 EVPN_Overlay_Peering
Ma1                            up             up                 oob_management
```
## show ip interface brief

```
Address 
Interface       IP Address           Status     Protocol         MTU    Owner   
--------------- -------------------- ---------- ------------ ---------- ------- 
Ethernet1       10.10.100.2/31       up         up              1500            
Ethernet2       10.10.100.6/31       up         up              1500            
Ethernet3       10.10.100.10/31      up         up              1500            
Ethernet4       10.10.100.14/31      up         up              1500            
Loopback0       192.168.100.2/32     up         up             65535            
Management1     172.30.30.212/24     up         up              1500
```
## show lldp neighbors

```
Last table change time   : 0:27:27 ago
Number of table inserts  : 5
Number of table deletes  : 0
Number of table drops    : 0
Number of table age-outs : 0

Port          Neighbor Device ID        Neighbor Port ID    TTL 
---------- ------------------------- ---------------------- --- 
Et1           DC-LEAF1.homelab.io       Ethernet2           120 
Et2           DC-LEAF2.homelab.io       Ethernet2           120 
Et3           DC-LEAF3.homelab.io       Ethernet2           120 
Et4           DC-LEAF4.homelab.io       Ethernet2           120 
Ma1           mgmt-sw                   Ethernet8           120
```
## show running-config

```
! Command: show running-config
! device: DC-SPINE2 (vEOS, EOS-4.25.5M)
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
hostname DC-SPINE2
ip name-server vrf mgmt 1.1.1.1
ip name-server vrf mgmt 172.30.30.6
dns domain homelab.io
!
ntp local-interface vrf mgmt Management1
ntp server vrf mgmt time.google.com prefer iburst
!
spanning-tree mode none
!
clock timezone America/Toronto
!
vrf instance mgmt
!
interface Ethernet1
   description P2P_LINK_TO_DC-LEAF1_Ethernet2
   no switchport
   ip address 10.10.100.2/31
!
interface Ethernet2
   description P2P_LINK_TO_DC-LEAF2_Ethernet2
   no switchport
   ip address 10.10.100.6/31
!
interface Ethernet3
   description P2P_LINK_TO_DC-LEAF3_Ethernet2
   no switchport
   ip address 10.10.100.10/31
!
interface Ethernet4
   description P2P_LINK_TO_DC-LEAF4_Ethernet2
   no switchport
   ip address 10.10.100.14/31
!
interface Ethernet5
!
interface Ethernet6
!
interface Ethernet7
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
   ip address 192.168.100.2/32
!
interface Management1
   description oob_management
   vrf mgmt
   ip address 172.30.30.212/24
!
ip routing
no ip routing vrf mgmt
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 192.168.100.0/24 eq 32
!
ip route vrf mgmt 0.0.0.0/0 172.30.30.1
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
!
router bfd
   multihop interval 1200 min-rx 1200 multiplier 3
!
router bgp 65100
   router-id 192.168.100.2
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS next-hop-unchanged
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS password 7 q+VNViP5i4rVjW1cxFv2wA==
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 10.10.100.3 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.10.100.3 remote-as 65101
   neighbor 10.10.100.3 description DC-LEAF1_Ethernet2
   neighbor 10.10.100.7 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.10.100.7 remote-as 65102
   neighbor 10.10.100.7 description DC-LEAF2_Ethernet2
   neighbor 10.10.100.11 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.10.100.11 remote-as 65103
   neighbor 10.10.100.11 description DC-LEAF3_Ethernet2
   neighbor 10.10.100.15 peer group IPv4-UNDERLAY-PEERS
   neighbor 10.10.100.15 remote-as 65104
   neighbor 10.10.100.15 description DC-LEAF4_Ethernet2
   neighbor 192.168.100.3 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.100.3 remote-as 65101
   neighbor 192.168.100.3 description DC-LEAF1
   neighbor 192.168.100.4 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.100.4 remote-as 65102
   neighbor 192.168.100.4 description DC-LEAF2
   neighbor 192.168.100.5 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.100.5 remote-as 65103
   neighbor 192.168.100.5 description DC-LEAF3
   neighbor 192.168.100.6 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.100.6 remote-as 65104
   neighbor 192.168.100.6 description DC-LEAF4
   redistribute connected route-map RM-CONN-2-BGP
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
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
Hardware MAC address: 5001.22d5.315b
System MAC address: 5001.22d5.315b

Software image version: 4.25.5M
Architecture: i686
Internal build version: 4.25.5M-23663359.4255M
Internal build ID: 60baa7f9-12cb-41d2-ad7d-b6b2fcccfa92

Uptime: 0 weeks, 0 days, 0 hours and 30 minutes
Total memory: 4002604 kB
Free memory: 3048180 kB
```
