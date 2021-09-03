# DC_FABRIC

# Table of Contents
<!-- toc -->

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Overlay Loopback Interfaces (BGP EVPN Peering)](#overlay-loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (Leafs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-leafs-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

<!-- toc -->
# Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision |
| --- | ---- | ---- | ------------- | -------- | -------------------------- |
| DC_FABRIC | l3leaf | DC-LEAF1 | 172.30.30.213/24 | vEOS-LAB | Provisioned |
| DC_FABRIC | l3leaf | DC-LEAF2 | 172.30.30.214/24 | vEOS-LAB | Provisioned |
| DC_FABRIC | l3leaf | DC-LEAF3 | 172.30.30.215/24 | vEOS-LAB | Provisioned |
| DC_FABRIC | l3leaf | DC-LEAF4 | 172.30.30.216/24 | vEOS-LAB | Provisioned |
| DC_FABRIC | spine | DC-SPINE1 | 172.30.30.211/24 | vEOS-LAB | Provisioned |
| DC_FABRIC | spine | DC-SPINE2 | 172.30.30.212/24 | vEOS-LAB | Provisioned |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

## Fabric Switches with inband Management IP
| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

# Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | DC-LEAF1 | Ethernet1 | spine | DC-SPINE1 | Ethernet1 |
| l3leaf | DC-LEAF1 | Ethernet2 | spine | DC-SPINE2 | Ethernet1 |
| l3leaf | DC-LEAF2 | Ethernet1 | spine | DC-SPINE1 | Ethernet2 |
| l3leaf | DC-LEAF2 | Ethernet2 | spine | DC-SPINE2 | Ethernet2 |
| l3leaf | DC-LEAF3 | Ethernet1 | spine | DC-SPINE1 | Ethernet3 |
| l3leaf | DC-LEAF3 | Ethernet2 | spine | DC-SPINE2 | Ethernet3 |
| l3leaf | DC-LEAF4 | Ethernet1 | spine | DC-SPINE1 | Ethernet4 |
| l3leaf | DC-LEAF4 | Ethernet2 | spine | DC-SPINE2 | Ethernet4 |

# Fabric IP Allocation

## Fabric Point-To-Point Links

| P2P Summary | Available Addresses | Assigned addresses | Assigned Address % |
| ----------- | ------------------- | ------------------ | ------------------ |
| 10.10.100.0/24 | 256 | 16 | 6.25 % |

## Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| DC-LEAF1 | Ethernet1 | 10.10.100.1/31 | DC-SPINE1 | Ethernet1 | 10.10.100.0/31 |
| DC-LEAF1 | Ethernet2 | 10.10.100.3/31 | DC-SPINE2 | Ethernet1 | 10.10.100.2/31 |
| DC-LEAF2 | Ethernet1 | 10.10.100.5/31 | DC-SPINE1 | Ethernet2 | 10.10.100.4/31 |
| DC-LEAF2 | Ethernet2 | 10.10.100.7/31 | DC-SPINE2 | Ethernet2 | 10.10.100.6/31 |
| DC-LEAF3 | Ethernet1 | 10.10.100.9/31 | DC-SPINE1 | Ethernet3 | 10.10.100.8/31 |
| DC-LEAF3 | Ethernet2 | 10.10.100.11/31 | DC-SPINE2 | Ethernet3 | 10.10.100.10/31 |
| DC-LEAF4 | Ethernet1 | 10.10.100.13/31 | DC-SPINE1 | Ethernet4 | 10.10.100.12/31 |
| DC-LEAF4 | Ethernet2 | 10.10.100.15/31 | DC-SPINE2 | Ethernet4 | 10.10.100.14/31 |

## Overlay Loopback Interfaces (BGP EVPN Peering)

| Overlay Loopback Summary | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------------ | ------------------- | ------------------ | ------------------ |
| 192.168.100.0/24 | 256 | 6 | 2.35 % |

## Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| DC_FABRIC | DC-LEAF1 | 192.168.100.3/32 |
| DC_FABRIC | DC-LEAF2 | 192.168.100.4/32 |
| DC_FABRIC | DC-LEAF3 | 192.168.100.5/32 |
| DC_FABRIC | DC-LEAF4 | 192.168.100.6/32 |
| DC_FABRIC | DC-SPINE1 | 192.168.100.1/32 |
| DC_FABRIC | DC-SPINE2 | 192.168.100.2/32 |

## VTEP Loopback VXLAN Tunnel Source Interfaces (Leafs Only)

| VTEP Loopback Summary | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 192.168.101.0/24 | 256 | 4 | 1.57 % |

## VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| DC_FABRIC | DC-LEAF1 | 192.168.101.3/32 |
| DC_FABRIC | DC-LEAF2 | 192.168.101.4/32 |
| DC_FABRIC | DC-LEAF3 | 192.168.101.5/32 |
| DC_FABRIC | DC-LEAF4 | 192.168.101.6/32 |
