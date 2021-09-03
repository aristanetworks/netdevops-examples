
# Validate State Report

**Table of Contents:**

- [Validate State Report](validate-state-report)
  - [Test Results Summary](#test-results-summary)
  - [Failed Test Results Summary](#failed-test-results-summary)
  - [All Test Results](#all-test-results)

## Test Results Summary

### Summary Totals

| Total Tests | Total Tests Passed | Total Tests Failed |
| ----------- | ------------------ | ------------------ |
| 215 | 215 | 0 |

### Summary Totals Devices Under Tests

| DUT | Total Tests | Tests Passed | Tests Failed | Categories Failed |
| --- | ----------- | ------------ | ------------ | ----------------- |
| DC-LEAF1 |  38 | 38 | 0 | - |
| DC-LEAF2 |  40 | 40 | 0 | - |
| DC-LEAF3 |  41 | 41 | 0 | - |
| DC-LEAF4 |  34 | 34 | 0 | - |
| DC-SPINE1 |  31 | 31 | 0 | - |
| DC-SPINE2 |  31 | 31 | 0 | - |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed |
| ------------- | ----------- | ------------ | ------------ |
| NTP |  6 | 6 | 0 |
| Interface State |  75 | 75 | 0 |
| LLDP Topology |  16 | 16 | 0 |
| IP Reachability |  16 | 16 | 0 |
| BGP |  38 | 38 | 0 |
| Routing Table |  40 | 40 | 0 |
| Loopback0 Reachability |  24 | 24 | 0 |

## Failed Test Results Summary

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |

## All Test Results

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 1 | DC-LEAF1 | NTP | Synchronised with NTP server | NTP | PASS |  |
| 2 | DC-LEAF2 | NTP | Synchronised with NTP server | NTP | PASS |  |
| 3 | DC-LEAF3 | NTP | Synchronised with NTP server | NTP | PASS |  |
| 4 | DC-LEAF4 | NTP | Synchronised with NTP server | NTP | PASS |  |
| 5 | DC-SPINE1 | NTP | Synchronised with NTP server | NTP | PASS |  |
| 6 | DC-SPINE2 | NTP | Synchronised with NTP server | NTP | PASS |  |
| 7 | DC-LEAF1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_DC-SPINE1_Ethernet1 | PASS |  |
| 8 | DC-LEAF1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_DC-SPINE2_Ethernet1 | PASS |  |
| 9 | DC-LEAF1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet5 - server01_E1 | PASS |  |
| 10 | DC-LEAF1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet6 - server02_E1 | PASS |  |
| 11 | DC-LEAF1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet7 - server03_E1 | PASS |  |
| 12 | DC-LEAF2 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_DC-SPINE1_Ethernet2 | PASS |  |
| 13 | DC-LEAF2 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_DC-SPINE2_Ethernet2 | PASS |  |
| 14 | DC-LEAF2 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet5 - server01_E2 | PASS |  |
| 15 | DC-LEAF2 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet6 - server02_E2 | PASS |  |
| 16 | DC-LEAF2 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet7 - server03_E2 | PASS |  |
| 17 | DC-LEAF2 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet8 - server04_E1 | PASS |  |
| 18 | DC-LEAF3 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_DC-SPINE1_Ethernet3 | PASS |  |
| 19 | DC-LEAF3 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_DC-SPINE2_Ethernet3 | PASS |  |
| 20 | DC-LEAF3 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet7 - server03_E3 | PASS |  |
| 21 | DC-LEAF3 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet8 - server04_E2 | PASS |  |
| 22 | DC-LEAF3 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet5 - server05_E1 | PASS |  |
| 23 | DC-LEAF3 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet6 - server06_E1 | PASS |  |
| 24 | DC-LEAF4 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_DC-SPINE1_Ethernet4 | PASS |  |
| 25 | DC-LEAF4 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_DC-SPINE2_Ethernet4 | PASS |  |
| 26 | DC-LEAF4 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet5 - server05_E2 | PASS |  |
| 27 | DC-LEAF4 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet6 - server06_E2 | PASS |  |
| 28 | DC-SPINE1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_DC-LEAF1_Ethernet1 | PASS |  |
| 29 | DC-SPINE1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_DC-LEAF2_Ethernet1 | PASS |  |
| 30 | DC-SPINE1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_DC-LEAF3_Ethernet1 | PASS |  |
| 31 | DC-SPINE1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_DC-LEAF4_Ethernet1 | PASS |  |
| 32 | DC-SPINE2 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_DC-LEAF1_Ethernet2 | PASS |  |
| 33 | DC-SPINE2 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_DC-LEAF2_Ethernet2 | PASS |  |
| 34 | DC-SPINE2 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_DC-LEAF3_Ethernet2 | PASS |  |
| 35 | DC-SPINE2 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_DC-LEAF4_Ethernet2 | PASS |  |
| 36 | DC-LEAF1 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel5 - server01_PortChannel | PASS |  |
| 37 | DC-LEAF1 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel6 - server02_PortChannel | PASS |  |
| 38 | DC-LEAF1 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel7 - server03_PortChannel | PASS |  |
| 39 | DC-LEAF2 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel5 - server01_PortChannel | PASS |  |
| 40 | DC-LEAF2 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel6 - server02_PortChannel | PASS |  |
| 41 | DC-LEAF2 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel7 - server03_PortChannel | PASS |  |
| 42 | DC-LEAF2 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel8 - server04_PortChannel | PASS |  |
| 43 | DC-LEAF3 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel7 - server03_PortChannel | PASS |  |
| 44 | DC-LEAF3 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel8 - server04_PortChannel | PASS |  |
| 45 | DC-LEAF3 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel5 - server05_PortChannel | PASS |  |
| 46 | DC-LEAF3 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel6 - server06_PortChannel | PASS |  |
| 47 | DC-LEAF4 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel5 - server05_PortChannel | PASS |  |
| 48 | DC-LEAF4 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel6 - server06_PortChannel | PASS |  |
| 49 | DC-LEAF1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan10 - Tenant_blue_compute | PASS |  |
| 50 | DC-LEAF1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan20 - Tenant_green_compute | PASS |  |
| 51 | DC-LEAF1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan30 - Tenant_green_storage | PASS |  |
| 52 | DC-LEAF2 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan10 - Tenant_blue_compute | PASS |  |
| 53 | DC-LEAF2 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan20 - Tenant_green_compute | PASS |  |
| 54 | DC-LEAF2 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan30 - Tenant_green_storage | PASS |  |
| 55 | DC-LEAF3 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan10 - Tenant_blue_compute | PASS |  |
| 56 | DC-LEAF3 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan50 - Tenant_blue_storage | PASS |  |
| 57 | DC-LEAF3 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan30 - Tenant_green_storage | PASS |  |
| 58 | DC-LEAF3 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan40 - Tenant_red_storage | PASS |  |
| 59 | DC-LEAF4 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan50 - Tenant_blue_storage | PASS |  |
| 60 | DC-LEAF4 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan40 - Tenant_red_storage | PASS |  |
| 61 | DC-LEAF1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS |  |
| 62 | DC-LEAF2 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS |  |
| 63 | DC-LEAF3 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS |  |
| 64 | DC-LEAF4 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS |  |
| 65 | DC-LEAF1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS |  |
| 66 | DC-LEAF1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS |  |
| 67 | DC-LEAF1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback100 - Tenant_blue_vrf_VTEP_DIAGNOSTICS | PASS |  |
| 68 | DC-LEAF1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback200 - Tenant_green_vrf_VTEP_DIAGNOSTICS | PASS |  |
| 69 | DC-LEAF2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS |  |
| 70 | DC-LEAF2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS |  |
| 71 | DC-LEAF2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback100 - Tenant_blue_vrf_VTEP_DIAGNOSTICS | PASS |  |
| 72 | DC-LEAF2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback200 - Tenant_green_vrf_VTEP_DIAGNOSTICS | PASS |  |
| 73 | DC-LEAF3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS |  |
| 74 | DC-LEAF3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS |  |
| 75 | DC-LEAF3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback100 - Tenant_blue_vrf_VTEP_DIAGNOSTICS | PASS |  |
| 76 | DC-LEAF3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback200 - Tenant_green_vrf_VTEP_DIAGNOSTICS | PASS |  |
| 77 | DC-LEAF4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS |  |
| 78 | DC-LEAF4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS |  |
| 79 | DC-LEAF4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback100 - Tenant_blue_vrf_VTEP_DIAGNOSTICS | PASS |  |
| 80 | DC-SPINE1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS |  |
| 81 | DC-SPINE2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS |  |
| 82 | DC-LEAF1 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet1 - remote: DC-SPINE1_Ethernet1 | PASS |  |
| 83 | DC-LEAF1 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet2 - remote: DC-SPINE2_Ethernet1 | PASS |  |
| 84 | DC-LEAF2 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet1 - remote: DC-SPINE1_Ethernet2 | PASS |  |
| 85 | DC-LEAF2 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet2 - remote: DC-SPINE2_Ethernet2 | PASS |  |
| 86 | DC-LEAF3 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet1 - remote: DC-SPINE1_Ethernet3 | PASS |  |
| 87 | DC-LEAF3 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet2 - remote: DC-SPINE2_Ethernet3 | PASS |  |
| 88 | DC-LEAF4 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet1 - remote: DC-SPINE1_Ethernet4 | PASS |  |
| 89 | DC-LEAF4 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet2 - remote: DC-SPINE2_Ethernet4 | PASS |  |
| 90 | DC-SPINE1 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet1 - remote: DC-LEAF1_Ethernet1 | PASS |  |
| 91 | DC-SPINE1 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet2 - remote: DC-LEAF2_Ethernet1 | PASS |  |
| 92 | DC-SPINE1 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet3 - remote: DC-LEAF3_Ethernet1 | PASS |  |
| 93 | DC-SPINE1 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet4 - remote: DC-LEAF4_Ethernet1 | PASS |  |
| 94 | DC-SPINE2 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet1 - remote: DC-LEAF1_Ethernet2 | PASS |  |
| 95 | DC-SPINE2 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet2 - remote: DC-LEAF2_Ethernet2 | PASS |  |
| 96 | DC-SPINE2 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet3 - remote: DC-LEAF3_Ethernet2 | PASS |  |
| 97 | DC-SPINE2 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet4 - remote: DC-LEAF4_Ethernet2 | PASS |  |
| 98 | DC-LEAF1 | IP Reachability | ip reachability test p2p links | Source: DC-LEAF1_Ethernet1 - Destination: DC-SPINE1_Ethernet1 | PASS |  |
| 99 | DC-LEAF1 | IP Reachability | ip reachability test p2p links | Source: DC-LEAF1_Ethernet2 - Destination: DC-SPINE2_Ethernet1 | PASS |  |
| 100 | DC-LEAF2 | IP Reachability | ip reachability test p2p links | Source: DC-LEAF2_Ethernet1 - Destination: DC-SPINE1_Ethernet2 | PASS |  |
| 101 | DC-LEAF2 | IP Reachability | ip reachability test p2p links | Source: DC-LEAF2_Ethernet2 - Destination: DC-SPINE2_Ethernet2 | PASS |  |
| 102 | DC-LEAF3 | IP Reachability | ip reachability test p2p links | Source: DC-LEAF3_Ethernet1 - Destination: DC-SPINE1_Ethernet3 | PASS |  |
| 103 | DC-LEAF3 | IP Reachability | ip reachability test p2p links | Source: DC-LEAF3_Ethernet2 - Destination: DC-SPINE2_Ethernet3 | PASS |  |
| 104 | DC-LEAF4 | IP Reachability | ip reachability test p2p links | Source: DC-LEAF4_Ethernet1 - Destination: DC-SPINE1_Ethernet4 | PASS |  |
| 105 | DC-LEAF4 | IP Reachability | ip reachability test p2p links | Source: DC-LEAF4_Ethernet2 - Destination: DC-SPINE2_Ethernet4 | PASS |  |
| 106 | DC-SPINE1 | IP Reachability | ip reachability test p2p links | Source: DC-SPINE1_Ethernet1 - Destination: DC-LEAF1_Ethernet1 | PASS |  |
| 107 | DC-SPINE1 | IP Reachability | ip reachability test p2p links | Source: DC-SPINE1_Ethernet2 - Destination: DC-LEAF2_Ethernet1 | PASS |  |
| 108 | DC-SPINE1 | IP Reachability | ip reachability test p2p links | Source: DC-SPINE1_Ethernet3 - Destination: DC-LEAF3_Ethernet1 | PASS |  |
| 109 | DC-SPINE1 | IP Reachability | ip reachability test p2p links | Source: DC-SPINE1_Ethernet4 - Destination: DC-LEAF4_Ethernet1 | PASS |  |
| 110 | DC-SPINE2 | IP Reachability | ip reachability test p2p links | Source: DC-SPINE2_Ethernet1 - Destination: DC-LEAF1_Ethernet2 | PASS |  |
| 111 | DC-SPINE2 | IP Reachability | ip reachability test p2p links | Source: DC-SPINE2_Ethernet2 - Destination: DC-LEAF2_Ethernet2 | PASS |  |
| 112 | DC-SPINE2 | IP Reachability | ip reachability test p2p links | Source: DC-SPINE2_Ethernet3 - Destination: DC-LEAF3_Ethernet2 | PASS |  |
| 113 | DC-SPINE2 | IP Reachability | ip reachability test p2p links | Source: DC-SPINE2_Ethernet4 - Destination: DC-LEAF4_Ethernet2 | PASS |  |
| 114 | DC-LEAF1 | BGP | ArBGP is configured and operating | ArBGP | PASS |  |
| 115 | DC-LEAF2 | BGP | ArBGP is configured and operating | ArBGP | PASS |  |
| 116 | DC-LEAF3 | BGP | ArBGP is configured and operating | ArBGP | PASS |  |
| 117 | DC-LEAF4 | BGP | ArBGP is configured and operating | ArBGP | PASS |  |
| 118 | DC-SPINE1 | BGP | ArBGP is configured and operating | ArBGP | PASS |  |
| 119 | DC-SPINE2 | BGP | ArBGP is configured and operating | ArBGP | PASS |  |
| 120 | DC-LEAF1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.100.0 | PASS |  |
| 121 | DC-LEAF1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.100.2 | PASS |  |
| 122 | DC-LEAF2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.100.4 | PASS |  |
| 123 | DC-LEAF2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.100.6 | PASS |  |
| 124 | DC-LEAF3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.100.8 | PASS |  |
| 125 | DC-LEAF3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.100.10 | PASS |  |
| 126 | DC-LEAF4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.100.12 | PASS |  |
| 127 | DC-LEAF4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.100.14 | PASS |  |
| 128 | DC-SPINE1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.100.1 | PASS |  |
| 129 | DC-SPINE1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.100.5 | PASS |  |
| 130 | DC-SPINE1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.100.9 | PASS |  |
| 131 | DC-SPINE1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.100.13 | PASS |  |
| 132 | DC-SPINE2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.100.3 | PASS |  |
| 133 | DC-SPINE2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.100.7 | PASS |  |
| 134 | DC-SPINE2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.100.11 | PASS |  |
| 135 | DC-SPINE2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.10.100.15 | PASS |  |
| 136 | DC-LEAF1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.100.1 | PASS |  |
| 137 | DC-LEAF1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.100.2 | PASS |  |
| 138 | DC-LEAF2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.100.1 | PASS |  |
| 139 | DC-LEAF2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.100.2 | PASS |  |
| 140 | DC-LEAF3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.100.1 | PASS |  |
| 141 | DC-LEAF3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.100.2 | PASS |  |
| 142 | DC-LEAF4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.100.1 | PASS |  |
| 143 | DC-LEAF4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.100.2 | PASS |  |
| 144 | DC-SPINE1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.100.3 | PASS |  |
| 145 | DC-SPINE1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.100.4 | PASS |  |
| 146 | DC-SPINE1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.100.5 | PASS |  |
| 147 | DC-SPINE1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.100.6 | PASS |  |
| 148 | DC-SPINE2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.100.3 | PASS |  |
| 149 | DC-SPINE2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.100.4 | PASS |  |
| 150 | DC-SPINE2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.100.5 | PASS |  |
| 151 | DC-SPINE2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.100.6 | PASS |  |
| 152 | DC-LEAF1 | Routing Table | Remote Lo1 address | 192.168.101.3 | PASS |  |
| 153 | DC-LEAF1 | Routing Table | Remote Lo1 address | 192.168.101.4 | PASS |  |
| 154 | DC-LEAF1 | Routing Table | Remote Lo1 address | 192.168.101.5 | PASS |  |
| 155 | DC-LEAF1 | Routing Table | Remote Lo1 address | 192.168.101.6 | PASS |  |
| 156 | DC-LEAF2 | Routing Table | Remote Lo1 address | 192.168.101.3 | PASS |  |
| 157 | DC-LEAF2 | Routing Table | Remote Lo1 address | 192.168.101.4 | PASS |  |
| 158 | DC-LEAF2 | Routing Table | Remote Lo1 address | 192.168.101.5 | PASS |  |
| 159 | DC-LEAF2 | Routing Table | Remote Lo1 address | 192.168.101.6 | PASS |  |
| 160 | DC-LEAF3 | Routing Table | Remote Lo1 address | 192.168.101.3 | PASS |  |
| 161 | DC-LEAF3 | Routing Table | Remote Lo1 address | 192.168.101.4 | PASS |  |
| 162 | DC-LEAF3 | Routing Table | Remote Lo1 address | 192.168.101.5 | PASS |  |
| 163 | DC-LEAF3 | Routing Table | Remote Lo1 address | 192.168.101.6 | PASS |  |
| 164 | DC-LEAF4 | Routing Table | Remote Lo1 address | 192.168.101.3 | PASS |  |
| 165 | DC-LEAF4 | Routing Table | Remote Lo1 address | 192.168.101.4 | PASS |  |
| 166 | DC-LEAF4 | Routing Table | Remote Lo1 address | 192.168.101.5 | PASS |  |
| 167 | DC-LEAF4 | Routing Table | Remote Lo1 address | 192.168.101.6 | PASS |  |
| 168 | DC-LEAF1 | Routing Table | Remote Lo0 address | 192.168.100.3 | PASS |  |
| 169 | DC-LEAF1 | Routing Table | Remote Lo0 address | 192.168.100.4 | PASS |  |
| 170 | DC-LEAF1 | Routing Table | Remote Lo0 address | 192.168.100.5 | PASS |  |
| 171 | DC-LEAF1 | Routing Table | Remote Lo0 address | 192.168.100.6 | PASS |  |
| 172 | DC-LEAF2 | Routing Table | Remote Lo0 address | 192.168.100.3 | PASS |  |
| 173 | DC-LEAF2 | Routing Table | Remote Lo0 address | 192.168.100.4 | PASS |  |
| 174 | DC-LEAF2 | Routing Table | Remote Lo0 address | 192.168.100.5 | PASS |  |
| 175 | DC-LEAF2 | Routing Table | Remote Lo0 address | 192.168.100.6 | PASS |  |
| 176 | DC-LEAF3 | Routing Table | Remote Lo0 address | 192.168.100.3 | PASS |  |
| 177 | DC-LEAF3 | Routing Table | Remote Lo0 address | 192.168.100.4 | PASS |  |
| 178 | DC-LEAF3 | Routing Table | Remote Lo0 address | 192.168.100.5 | PASS |  |
| 179 | DC-LEAF3 | Routing Table | Remote Lo0 address | 192.168.100.6 | PASS |  |
| 180 | DC-LEAF4 | Routing Table | Remote Lo0 address | 192.168.100.3 | PASS |  |
| 181 | DC-LEAF4 | Routing Table | Remote Lo0 address | 192.168.100.4 | PASS |  |
| 182 | DC-LEAF4 | Routing Table | Remote Lo0 address | 192.168.100.5 | PASS |  |
| 183 | DC-LEAF4 | Routing Table | Remote Lo0 address | 192.168.100.6 | PASS |  |
| 184 | DC-SPINE1 | Routing Table | Remote Lo0 address | 192.168.100.3 | PASS |  |
| 185 | DC-SPINE1 | Routing Table | Remote Lo0 address | 192.168.100.4 | PASS |  |
| 186 | DC-SPINE1 | Routing Table | Remote Lo0 address | 192.168.100.5 | PASS |  |
| 187 | DC-SPINE1 | Routing Table | Remote Lo0 address | 192.168.100.6 | PASS |  |
| 188 | DC-SPINE2 | Routing Table | Remote Lo0 address | 192.168.100.3 | PASS |  |
| 189 | DC-SPINE2 | Routing Table | Remote Lo0 address | 192.168.100.4 | PASS |  |
| 190 | DC-SPINE2 | Routing Table | Remote Lo0 address | 192.168.100.5 | PASS |  |
| 191 | DC-SPINE2 | Routing Table | Remote Lo0 address | 192.168.100.6 | PASS |  |
| 192 | DC-LEAF1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC-LEAF1 - 192.168.100.3 Destination: 192.168.100.3 | PASS |  |
| 193 | DC-LEAF1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC-LEAF1 - 192.168.100.3 Destination: 192.168.100.4 | PASS |  |
| 194 | DC-LEAF1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC-LEAF1 - 192.168.100.3 Destination: 192.168.100.5 | PASS |  |
| 195 | DC-LEAF1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC-LEAF1 - 192.168.100.3 Destination: 192.168.100.6 | PASS |  |
| 196 | DC-LEAF2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC-LEAF2 - 192.168.100.4 Destination: 192.168.100.3 | PASS |  |
| 197 | DC-LEAF2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC-LEAF2 - 192.168.100.4 Destination: 192.168.100.4 | PASS |  |
| 198 | DC-LEAF2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC-LEAF2 - 192.168.100.4 Destination: 192.168.100.5 | PASS |  |
| 199 | DC-LEAF2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC-LEAF2 - 192.168.100.4 Destination: 192.168.100.6 | PASS |  |
| 200 | DC-LEAF3 | Loopback0 Reachability | Loopback0 Reachability | Source: DC-LEAF3 - 192.168.100.5 Destination: 192.168.100.3 | PASS |  |
| 201 | DC-LEAF3 | Loopback0 Reachability | Loopback0 Reachability | Source: DC-LEAF3 - 192.168.100.5 Destination: 192.168.100.4 | PASS |  |
| 202 | DC-LEAF3 | Loopback0 Reachability | Loopback0 Reachability | Source: DC-LEAF3 - 192.168.100.5 Destination: 192.168.100.5 | PASS |  |
| 203 | DC-LEAF3 | Loopback0 Reachability | Loopback0 Reachability | Source: DC-LEAF3 - 192.168.100.5 Destination: 192.168.100.6 | PASS |  |
| 204 | DC-LEAF4 | Loopback0 Reachability | Loopback0 Reachability | Source: DC-LEAF4 - 192.168.100.6 Destination: 192.168.100.3 | PASS |  |
| 205 | DC-LEAF4 | Loopback0 Reachability | Loopback0 Reachability | Source: DC-LEAF4 - 192.168.100.6 Destination: 192.168.100.4 | PASS |  |
| 206 | DC-LEAF4 | Loopback0 Reachability | Loopback0 Reachability | Source: DC-LEAF4 - 192.168.100.6 Destination: 192.168.100.5 | PASS |  |
| 207 | DC-LEAF4 | Loopback0 Reachability | Loopback0 Reachability | Source: DC-LEAF4 - 192.168.100.6 Destination: 192.168.100.6 | PASS |  |
| 208 | DC-SPINE1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC-SPINE1 - 192.168.100.1 Destination: 192.168.100.3 | PASS |  |
| 209 | DC-SPINE1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC-SPINE1 - 192.168.100.1 Destination: 192.168.100.4 | PASS |  |
| 210 | DC-SPINE1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC-SPINE1 - 192.168.100.1 Destination: 192.168.100.5 | PASS |  |
| 211 | DC-SPINE1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC-SPINE1 - 192.168.100.1 Destination: 192.168.100.6 | PASS |  |
| 212 | DC-SPINE2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC-SPINE2 - 192.168.100.2 Destination: 192.168.100.3 | PASS |  |
| 213 | DC-SPINE2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC-SPINE2 - 192.168.100.2 Destination: 192.168.100.4 | PASS |  |
| 214 | DC-SPINE2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC-SPINE2 - 192.168.100.2 Destination: 192.168.100.5 | PASS |  |
| 215 | DC-SPINE2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC-SPINE2 - 192.168.100.2 Destination: 192.168.100.6 | PASS |  |
