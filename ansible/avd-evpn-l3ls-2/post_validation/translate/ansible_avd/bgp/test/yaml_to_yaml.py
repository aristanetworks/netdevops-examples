from translate.tools import *


def default(src_filename, dst_filename):
    dut_show_data = load_yaml(src_filename)

    bgp_peer_dict = dict()

    for hostname, details in dut_show_data['duts'].items():

        if hostname not in bgp_peer_dict.keys():
            bgp_peer_dict.update({hostname: {
                'underlay': dict(),
                'evpn': dict()
            }})

        # add underlay peers
        if 'default' in details['show ip bgp summary']['vrfs']:
            for peer_ip, peer_details in details['show ip bgp summary']['vrfs']['default']['peers'].items():
                peer_state = peer_details['peerState']
                bgp_peer_dict[hostname]['underlay'].update({peer_ip: {'state': peer_state}})

        # add EVPN
        if 'default' in details['show bgp evpn summary']['vrfs']:
            for peer_ip, peer_details in details['show bgp evpn summary']['vrfs']['default']['peers'].items():
                peer_state = peer_details['peerState']
                bgp_peer_dict[hostname]['evpn'].update({peer_ip: {'state': peer_state}})

    write_yaml(dst_filename, bgp_peer_dict)
