import netdiff
import sys

def from_struct_config(structured_configs_dir):

    bgp_peer_dict = dict()
    struct_config_data = netdiff.read.yamls_from_dir(structured_configs_dir)
    for hostname, struct_config in struct_config_data.items():
        bgp_peer_dict.update({
            hostname: {
                'underlay': dict(),
                'evpn': dict()
            }
        })
        if 'router_bgp' in struct_config.keys():
            for bgp_peer_ip, bgp_peer_group_dict in struct_config['router_bgp']['neighbors'].items():
                peer_group_name = bgp_peer_group_dict['peer_group']
                if (peer_group_name == 'IPv4-UNDERLAY-PEERS') or (peer_group_name == 'MLAG-IPv4-UNDERLAY-PEER'):
                    bgp_peer_dict[hostname]['underlay'].update({
                        bgp_peer_ip: {'state': 'Established'}  # asn not supported due to listen-range
                    })
                elif peer_group_name == 'EVPN-OVERLAY-PEERS':
                    bgp_peer_dict[hostname]['evpn'].update({
                        bgp_peer_ip: {'state': 'Established'}  # asn not supported due to listen-range
                    })

    return bgp_peer_dict


if __name__ == "__main__":
    eval_check_list = [  # list all functions allowed for eval() here
        'from_struct_config',
    ]
    args = netdiff.tools.parsers.src_dst_parser()
    in_data = netdiff.read._from(args.src_format, args.src_filename)
    if args.case in eval_check_list:
        if not isinstance(in_data, str):
            out_data = eval(args.case + f'({in_data})')
        else:
            out_data = eval(args.case + f'("{in_data}")')
        netdiff.write.to_file(args.dst_filename, args.dst_format, out_data)
    else:
        sys.exit(f'ERROR: Specified case {args.case} is not supported!')
