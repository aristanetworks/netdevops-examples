
* [Introduction](#introduction)
  - [Test Setup](#test-setup)
  - [Deploy vEOS Arista EVPN/VXLAN fabric and ESXi hosts](#deploy-veos-arista-evpnvxlan-fabric-and-esxi-hosts)
  - [Deploy NSX-T Manager on ESXi3](#deploy-nsx-t-manager-on-esxi3)
  - [Deploy NSX-T Edge VM](#deploy-nsx-t-edge-vm)
  - [Configure BGP peering](#configure-bgp-peering)
  - [Configure BGP Route Re-Distribution](#configure-bgp-route-re-distribution)
  - [Configure BGP peering on EOS external Gateway](#configure-bgp-peering-on-eos-external-gateway)
  - [Control Plane Verification](#control-plane-verification)
  - [Data Plane Verification](#data-plane-verification)
  - [Useful Links](#useful-links)

**Introduction**

VMWare NSX-T 3.0 introduced support for EVPN Type-5 integration which allows efficient multi-tenant L3 exchange between VMWare NSX-T Edge and external gateways. The following graph should visualize life before and after the EVPN Type5 support:

![](https://eos.arista.com/wp-content/uploads/2020/05/Legacy-EVPN-Difference-2-1024x608.png)

Instead of having 802.1q trunk interface with L3 sub-interface per VRF, we now can have a single routed interface with just a single BGP EVPN session. This greatly reduces configuration overhead on both sides. This article will describe all necessary steps required to test this feature against Arista EOS devices.

## Test Setup

Let us assume we already have running EVPN/VXLAN fabric with Symmetric IRB (SIRB) as many customers already deployed EVPN/VXLAN in their data centers and just want to use existing infrastructure to deploy NSX-T. We are going to use one VLAN with SIRB 10.10.100.1/24 to get NSX-T Geneve overlay running on top of it. Strictly speaking we could use IP Fabric underlay to distribute NSX-T TEPs reachability to form Geneve overlay. Once we have Geneve traffic successfully forwarded through EVPN fabric, we will add NSX-T Edge Transport Node. NSX-T Edge is going to implement:

1. L3 multi-tenancy segmentation. Geneve Segment1 will be configured to be part of VRFA.
2. Route exchange between VRFA and external Arista Gateway using EVPN Type-5
3. Stitching two different data planes: Geneve and VXLAN

## ![](https://eos.arista.com/wp-content/uploads/2020/05/NSX3-EVPN-6-1024x717.jpeg)

Everything in that setup except physical EVPN GW is running within EVEng. NOTE: It is also possible to run EVPN GW as vEOS in EVEng. At the end of this exercise we should be able to have connectivity between end systems in Geneve Overlay (VM1 and VM2) and  workload connected to external Arista GW (VM3). Multi-tenancy must be honoured: both prefixes 192.168.1.0/24 from overlay and 192.168.200.0/24 must be confined only within VRFA.

## Deploy vEOS Arista EVPN/VXLAN fabric and ESXi hosts

Following Github repository has EVEng lab and vEOS configuration: [Github NSX-T 3.0 EVPN Type 5 Lab](https://github.com/mpergament/nsxt-evpn-eveng-lab).

![](https://eos.arista.com/wp-content/uploads/2020/05/EVEng-Topo.png)

pcs-esxi1 and pcs-esxi2 are going to be our Host Transport Nodes. VM1 will be running on pcs-esxi1 and VM2 pn pcs-esxi2. NSX-T Manager VM and NSX-T Edge VM will be running on pcs-esxi3. Deployment of ESXi hosts is outside the scope of this article.

Following screenshot shows allocated resources (RAM, vCPUs) for each node in the topology.

![](https://eos.arista.com/wp-content/uploads/2020/05/evenodes.png)

## Deploy NSX-T Manager on ESXi3

1. In the vSphere Client of esxi3, select **Create / Register VM**and follow the steps in [VMware NSX-T Manager Installation](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.0/installation/GUID-A65FE3DD-C4F1-47EC-B952-DEDF1A3DD0CF.html)
2. Login to the NSX-T Manager web console: https://<nsxmanager>:443 and proceed to " **System -> Fabric -> Transport Zones"**. Create new Overlay Transport Zone<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/tz1-creation.png)
3. Under " **System -> Fabric -> Nodes -> Host** " Transport Nodes click Add button:<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/tn1-creation-1.png)
4. Click NEXT and configure Host Transport Node:<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/tn1-config-1.png)<br>
In our setup both Transport Nodes have a single interface towards the EVPN fabric . That is why we set Uplink Profile to **nsx-edge-single-nic-uplink-profile**. TEP IP is set to 10.10.100.100 for this node. This is going to be used as outer Src IP Header. Finally uplink is mapped to physical NIC on ESXi. Repeat steps 4-5 for all your Host Transport Nodes.
5. Go to " **Networking -> Segments"** and add new Segment attached to the Transport Zone TZ1:<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/OverlayTZ.jpg)
6. Go to ESXi1 and ESXi2 and start one VM on each of them. Connect vNIC of VM to S2 segment:<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/overlay-vm-config.png)
7. Configure IP on VM1 to 192.168.1.10/24 and VM2 to 192.168.1.20/24. Ping VM2 from VM1. At this stage you should be done with the Overlay config.

## Deploy NSX-T Edge VM

1. In the vSphere Client of esxi3, select **Create / Register VM**and follow the steps in [VMWare NSX-T Edge Installation](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.0/installation/GUID-5EF2998C-4867-4DA6-B1C6-8A6F8EBCC411.html)
2. NSX-T Edge OVA comes with 4 interfaces. We are going to use first 3 interfaces:<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/nsxedge-vm-config.png)
3. As we deployed Edge VM from OVA you will need to go through following steps to add it to the NSX-T Manager:[How to join NSX-T Edge with management plane](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.0/installation/GUID-11BB4CF9-BC1D-4A76-A32A-AD4C98CBF25B.html)
4. Once added successfully you should see your Edge VM under " **System -> Fabric -> Nodes -> Edge Transport Nodes"**<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/edgenode-1-1024x184.png)
5. Under " **System -> Fabric -> Nodes -> Edge Clusters"** click Add button and add your single Edge node to cluster:
6. Configure the first Switch (connected to Overlay Transport Zone TZ1) on your Edge Node :<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/Edge-TN-SwitchOvelray-2.png)
7. Create new Uplink Profile BGP-PEERING under " **System -> Fabric -> Profiles"**:<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/UplinkProfileExtGW-2.png)
8. Configure the second Switch (connected to default VLAN Transport Zone **nsx-vlan-transportzone**) on your Edge Node :<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/Edge-TN-SwitchVLAN.png)
9. Go to " **Networking -> Segments"** and add new Segment attached to Transport Zone **nsx-vxlan-transportzone**:<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/GWsegment-config.png)
10. Create new VNI pool under " **Networking -> Setting -> VNI Pool"**:<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/vnipool.png)
11. Create Tier-0 Gateway under " **Networking -> Connectivity -> Tier-0″** (Pulldown Add Gateway):<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/Tier0GW-EVPN-Settings.png)
12. Create VRFA under " **Networking -> Connectivity -> Tier-0″** (Pulldown Add VRF):<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/tier0-AddVrf.png)
13. Configure VRFA:<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/tier0-vrfa-1.png)
14. Configure Route Targets 65000:10 (both import and export) for this VRFA:<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/vrfa-rts-1.png)
15. Attach interface on the Tier-0 GW towards external Arista GW Gateway under " **Networking -> Connectivity -> Tier-0″.** 192.168.150.1/24 is local peering IP on Edge, external GW will have 192.168.150.2/24.<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/gw0-extint.png)
16. Configure interface on external EOS GW:

```
interface Ethernet1
   description "to NSX-T Edge"
   mtu 9000
   speed forced 10000full
   no switchport
   ip address 192.168.150.2/24
```

At this point of time you should be able to ping 192.168.150.1 from EOS external GW.
17. Attach Tier-0 VRFA GW to Overlay Segment S2 as Default GW:<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/OverlaySegAttach.png)
18. Configure default route on both VM1 and VM2 to have next-hop of 192.168.1.1

## Configure BGP peering

1. Configure BGP under " **Networking -> Connectivity -> Tier-0 Gateways"** (NOT VRFA!):<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/bgp-tier0.png)
2. Configure BGP peer:<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/bgppeer.png)
3. Add both address families for BGP peering by clicking on blue number under Route Filter (see above):<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/bgpsaf-1.png)

## Configure BGP Route Re-Distribution

1. In both VRFA and Tier-0 GW configure following:<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/bgp-route-redis.png)<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/bgp-route-redis1.png)

## Configure BGP peering on EOS external Gateway

Relevant EOS configuration (Arista 7280SR2 was used in this setup):

```
interface Loopback0
   description BGP router-Id
   ip address 192.168.55.1/32
!
interface Loopback300
   vrf VRFA
   ip address 10.10.10.1/32
!
interface Vlan300
   vrf VRFA
   ip address 192.168.200.1/24
!
interface Vxlan1
   vxlan source-interface Loopback0
   vxlan udp-port 4789
   vxlan vrf VRFA vni 200000
!
hardware tcam
   system profile vxlan-routing
!
ip routing
ip routing vrf VRFA
!
ip prefix-list loopback
   seq 10 permit 192.168.55.1/32
!
route-map loopback permit 10
   match ip address prefix-list loopback
!
router bgp 65001
   router-id 192.168.55.1
   neighbor NSXTEDGE peer group
   neighbor NSXTEDGE bfd
   neighbor NSXTEDGE remote-as 65000
   neighbor NSXTEDGE send-community
   neighbor NSXTEDGE maximum-routes 0
   neighbor 192.168.150.1 peer group NSXTEDGE
   redistribute connected route-map loopback
   !
   address-family evpn
      neighbor NSXTEDGE activate
   !
   vrf VRFA
      rd 192.168.55.1:50001
      route-target import evpn 65000:10
      route-target export evpn 65000:10
      redistribute connected
```

## Control Plane Verification

1. Verify BGP session status in the NSX-T Manager:<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/bgpstatus.png)
2. Download the Forwarding Table:<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/vrfa-ftable.png)
3. Show downloaded Forwarding Table:<br>
![](https://eos.arista.com/wp-content/uploads/2020/05/fib-1.png)
4. Show BGP status on EOS GW:

```
show bfd peers
VRF name: default
-----------------
DstAddr        MyDisc    YourDisc  Interface     Type    LastUp LastDown  LastDiag    State
---------------- ------------- ------------ ---------------- --------- --------------------
192.168.150.1 3990680118 127459675 Ethernet1(81) normal 05/25/20 13:18 NA No Diagnostic Up

show  bgp  evpn  summary
BGP summary information for VRF default
Router identifier 192.168.55.1, local AS number 65001
Neighbor Status Codes: m - Under maintenance
  Neighbor         V  AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State   PfxRcd PfxAcc
  192.168.150.1    4  65000           3312      3897    0    0 10:03:49 Estab   1      1

show  bgp  neighbors 192.168.150.1 evpn  received-routes detail
BGP routing table information for VRF default
Router identifier 192.168.55.1, local AS number 65001
BGP routing table entry for ip-prefix 192.168.1.0/24, Route Distinguisher: 10.10.100.200:10
 Paths: 1 available
  65000
    192.168.150.1 from 192.168.150.1 (192.168.150.1)
      Origin INCOMPLETE, metric 0, localpref -, weight 0, valid, external, best
      Extended Community: Route-Target-AS:65000:10 TunnelEncap:tunnelTypeVxlan EvpnRouterMac:02:50:56:00:08:00
      VNI: 200000

show  bgp  neighbors 192.168.150.1 evpn  advertised-routes detail
BGP routing table information for VRF default
Router identifier 192.168.55.1, local AS number 65001
Update wait-install is disabled
BGP routing table entry for ip-prefix 10.10.10.1/32, Route Distinguisher: 192.168.55.1:50001
 Paths: 1 available
  65001
    192.168.55.1 from - (0.0.0.0)
      Origin IGP, metric -, localpref 100, weight 0, valid, local, best, redistributed (Connected)
      Extended Community: Route-Target-AS:65000:10 TunnelEncap:tunnelTypeVxlan EvpnRouterMac:98:5d:82:97:61:bf
      VNI: 200000
BGP routing table entry for ip-prefix 192.168.200.0/24, Route Distinguisher: 192.168.55.1:50001
 Paths: 1 available
  65001
    192.168.55.1 from - (0.0.0.0)
      Origin IGP, metric -, localpref 100, weight 0, valid, local, best, redistributed (Connected)
      Extended Community: Route-Target-AS:65000:10 TunnelEncap:tunnelTypeVxlan EvpnRouterMac:98:5d:82:97:61:bf
      VNI: 200000
```

5. Show BGP status on EDGE CLI:

```
pcs-nsxedge(tier0_sr)> get bgp neighbor summary
BFD States: NC - Not configured, AC - Activating,DC - Disconnected
            AD - Admin down, DW - Down, IN - Init,UP - Up
BGP summary information for VRF default for address-family: ipv4Unicast
Router ID: 192.168.150.1  Local AS: 65000

Neighbor                            AS          State Up/DownTime  BFD InMsgs  OutMsgs InPfx  OutPfx

192.168.150.2                       65001       Estab 1d01h27m     UP  1798    1534    2      3

BFD States: NC - Not configured, AC - Activating,DC - Disconnected
            AD - Admin down, DW - Down, IN - Init,UP - Up
BGP summary information for VRF default for address-family: l2VpnEvpn
Router ID: 192.168.150.1  Local AS: 65000

Neighbor                            AS          State Up/DownTime  BFD InMsgs  OutMsgs InPfx  OutPfx

192.168.150.2                       65001       Estab 1d01h27m     UP  1798    1534    2      3
```

```
pcs-nsxedge(tier0_sr)> get bgp evpn
BGP table version is 1, local router ID is 192.168.150.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
Origin codes: i - IGP, e - EGP, ? - incomplete
EVPN type-2 prefix: [2]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]
EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
EVPN type-4 prefix: [4]:[ESI]:[IPlen]:[OrigIP]
EVPN type-5 prefix: [5]:[EthTag]:[IPlen]:[IP]

   Network          Next Hop            Metric LocPrf Weight Path
Route Distinguisher: 10.10.100.200:10
*> [5]:[0]:[24]:[192.168.1.0]
                    192.168.150.1            0         32768 ?
Route Distinguisher: 192.168.55.1:50001
*> [5]:[0]:[24]:[192.168.200.0]
                    192.168.55.1                           0 65001 i
*> [5]:[0]:[32]:[10.10.10.1]
                    192.168.55.1                           0 65001 i

pcs-nsxedge(tier0_sr)> get bfd-sessions
BFD Session
Dest_port                     : 3784
Diag                          : No Diagnostic
Encap                         : vlan
Forwarding                    : last true (current true)
Interface                     : de8f9cfd-1750-409e-af7b-45daf6501b26
Keep-down                     : false
Last_cp_diag                  : No Diagnostic
Last_cp_rmt_diag              : No Diagnostic
Last_cp_rmt_state             : up
Last_cp_state                 : up
Last_fwd_state                : UP
Last_local_down_diag          : No Diagnostic
Last_remote_down_diag         : No Diagnostic
Last_up_time                  : 2020-05-25 13:18:48
Local_address                 : 192.168.150.1
Local_discr                   : 127459675
Min_rx_ttl                    : 255
Multiplier                    : 3
Received_remote_diag          : No Diagnostic
Received_remote_state         : up
Remote_address                : 192.168.150.2
Remote_admin_down             : false
Remote_diag                   : No Diagnostic
Remote_discr                  : 3990680118
Remote_min_rx_interval        : 300
Remote_min_tx_interval        : 300
Remote_multiplier             : 3
Remote_state                  : up
Router                        : 6c04ae47-9d26-4b8b-9c78-16da971dbc80
Router_down                   : false
Rx_cfg_min                    : 500
Rx_interval                   : 500
Service-link                  : false
Session_type                  : LR_PORT
State                         : up
Tx_cfg_min                    : 500
Tx_interval                   : 500
```

## Data Plane Verification

Ping VM1 from VM3:

```
VM3#ping 192.168.1.10 source 192.168.200.10
PING 192.168.1.10 (192.168.1.10) from 192.168.200.10 : 72(100) bytes of data.
80 bytes from 192.168.1.10: icmp_seq=1 ttl=62 time=119 ms
80 bytes from 192.168.1.10: icmp_seq=2 ttl=62 time=111 ms
80 bytes from 192.168.1.10: icmp_seq=3 ttl=62 time=105 ms
80 bytes from 192.168.1.10: icmp_seq=4 ttl=62 time=98.0 ms
80 bytes from 192.168.1.10: icmp_seq=5 ttl=62 time=91.2 ms

VM3#traceroute 192.168.1.10 source 192.168.200.10
traceroute to 192.168.1.10 (192.168.1.10), 30 hops max, 60 byte packets
 1  192.168.200.1 (192.168.200.1)  0.224 ms  0.212 ms  0.195 ms
 2  192.168.1.10 (192.168.1.10)  73.891 ms !X  76.826 ms !X  79.203 ms !X
```

## Useful Links

**EVPN Webinars**: [https://www.arista.com/en/company/news/webinars](https://www.arista.com/en/company/news/webinars)

**VMWare NSX-T Distributed Firewall Integration with Arista Policy Control Service**: [https://events.arista.com/virtual-cloud-builders-2020-data-centre-continuous-innovation](https://events.arista.com/virtual-cloud-builders-2020-data-centre-continuous-innovation)

