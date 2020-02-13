from translate.tools import *


def default(src_dir, dst_filename):
    bgp_peer_dict = dict()

    for filename in os.listdir(src_dir):
        if ('.yml' in filename) or ('.yaml' in filename):
            realpath = get_realpath(filename, src_dir)
            yaml_data = load_yaml(realpath)
            hostname = filename.split('.')[0]

            if hostname not in bgp_peer_dict.keys():
                bgp_peer_dict.update({hostname: {
                    'underlay': dict(),
                    'evpn': dict()
                }})

            if 'router_bgp' in yaml_data:
                for bgp_peer_ip, bgp_peer_group_dict in yaml_data['router_bgp']['neighbors'].items():
                    peer_group_name = bgp_peer_group_dict['peer_group']
                    if (peer_group_name == 'IPv4-UNDERLAY-PEERS') or (peer_group_name == 'MLAG-IPv4-UNDERLAY-PEER'):
                        bgp_peer_dict[hostname]['underlay'].update({
                            bgp_peer_ip: {'state': 'Established'}  # asn not supported due to listen-range
                        })
                    elif peer_group_name == 'EVPN-OVERLAY-PEERS':
                        bgp_peer_dict[hostname]['evpn'].update({
                            bgp_peer_ip: {'state': 'Established'}  # asn not supported due to listen-range
                        })

    write_yaml(dst_filename, bgp_peer_dict)
