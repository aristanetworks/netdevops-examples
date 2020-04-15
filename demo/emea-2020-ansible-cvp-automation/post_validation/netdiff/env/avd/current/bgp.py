import netdiff
import sys

def from_dut(in_data):

    bgp_peer_dict = dict()

    for hostname, details in in_data['duts'].items():

        if hostname not in bgp_peer_dict.keys():
            bgp_peer_dict.update({hostname: {
                'underlay': dict(),
                'evpn': dict()
            }})

        if 'default' in details['show ip bgp summary']['vrfs'].keys():

            # add underlay peers
            for peer_ip, peer_details in details['show ip bgp summary']['vrfs']['default']['peers'].items():
                peer_state = peer_details['peerState']
                bgp_peer_dict[hostname]['underlay'].update({peer_ip: {'state': peer_state}})

            # add EVPN
            for peer_ip, peer_details in details['show bgp evpn summary']['vrfs']['default']['peers'].items():
                peer_state = peer_details['peerState']
                bgp_peer_dict[hostname]['evpn'].update({peer_ip: {'state': peer_state}})

    return bgp_peer_dict


if __name__ == "__main__":
    eval_check_list = [  # list all functions allowed for eval() here
        'from_dut',
    ]
    args = netdiff.tools.parsers.src_dst_parser()
    in_data = netdiff.read._from(args.src_format, args.src_filename)
    if args.case in eval_check_list:
        out_data = eval(args.case + f'({in_data})')
        netdiff.write.to_file(args.dst_filename, args.dst_format, out_data)
    else:
        sys.exit(f'ERROR: Specified case {args.case} is not supported!')
