# DC1_FABRIC

## Table of Contents

- [DC1_FABRIC](#dc1fabric )
  - [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Topology](#fabric-topology)
  - [Fabric IP Allocation](#fabric-ip-allocation)
    - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
    - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
    - [Overlay Loopback Interfaces (BGP EVPN Peering)](#overlay-loopback-interfaces-bgp-evpn-peering)
    - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
    - [VTEP Loopback VXLAN Tunnel Source Interfaces (Leafs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-leafs-only)
    - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| Node | Management IP | Platform |
| ---- | ------------- | -------- |
| SPINE1 | 192.168.100.31/24 | 7280R |
| SPINE2 | 192.168.100.35/24 | 7280R |
| LEAF1A | 192.168.100.32/24 | 7280R |
| LEAF2A | 192.168.100.33/24 | 7280R |
| LEAF2B | 192.168.100.34/24 | 7280R |

## Fabric Topology

| Type | Leaf Node | Leaf Interface | Peer Node | Peer Interface |
| ---- | --------- | -------------- | --------- | -------------- |
| L3 Leaf | LEAF1A | Ethernet1 | SPINE1 | Ethernet1 |
| L3 Leaf | LEAF1A | Ethernet2 | SPINE2 | Ethernet1 |
| L3 Leaf | LEAF2A | Ethernet1 | SPINE1 | Ethernet2 |
| L3 Leaf | LEAF2A | Ethernet2 | SPINE2 | Ethernet2 |
| L3 Leaf | LEAF2B | Ethernet1 | SPINE1 | Ethernet3 |
| L3 Leaf | LEAF2B | Ethernet2 | SPINE2 | Ethernet3 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| P2P Summary | Available Addresses | Assigned addresses | Assigned Address % |
| ----------- | ------------------- | ------------------ | ------------------ |
| 10.1.1.0/24 | 256 | 12 | 4.69 % |

### Point-To-Point Links Node Allocation

| Leaf Node | Leaf Interface | Leaf IP Address | Spine Node | Spine Interface | Spine IP Address |
| --------- | -------------- | --------------- | ---------- | --------------- | ---------------- |
| LEAF1A | Ethernet1 | 10.1.1.33/31 | SPINE1 | Ethernet1 | 10.1.1.32/31 |
| LEAF1A | Ethernet2 | 10.1.1.35/31 | SPINE2 | Ethernet1 | 10.1.1.34/31 |
| LEAF2A | Ethernet1 | 10.1.1.73/31 | SPINE1 | Ethernet2 | 10.1.1.72/31 |
| LEAF2A | Ethernet2 | 10.1.1.75/31 | SPINE2 | Ethernet2 | 10.1.1.74/31 |
| LEAF2B | Ethernet1 | 10.1.1.77/31 | SPINE1 | Ethernet3 | 10.1.1.76/31 |
| LEAF2B | Ethernet2 | 10.1.1.79/31 | SPINE2 | Ethernet3 | 10.1.1.78/31 |

### Overlay Loopback Interfaces (BGP EVPN Peering)

| Overlay Loopback Summary | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------------ | ------------------- | ------------------ | ------------------ |
| 1.1.1.0/24 | 256 | 5 | 1.96 % |

### Loopback0 Interfaces Node Allocation

| Node | Loopback0 |
| ---- | --------- |
| SPINE1 | 1.1.1.1/32 |
| SPINE2 | 1.1.1.2/32 |
| LEAF1A | 1.1.1.11/32 |
| LEAF2A | 1.1.1.21/32 |
| LEAF2B | 1.1.1.22/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (Leafs Only)

| VTEP Loopback Summary | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 2.2.2.0/24 | 256 | 3 | 1.18 % |

### VTEP Loopback Node allocation

| Node | Loopback1 |
| ---- | --------- |
| LEAF1A | 2.2.2.11/32 |
| LEAF2A | 2.2.2.21/32 |
| LEAF2B | 2.2.2.21/32 |
