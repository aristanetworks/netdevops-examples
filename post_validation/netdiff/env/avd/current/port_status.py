import netdiff
import sys


def port_channel_status_from_dut(in_data):

    port_channel_status = dict()

    for hostname, d in in_data['duts'].items():

        if 'portChannels' in d['show port-channel summary'].keys():
            if len(d['show port-channel summary']['portChannels']):
                port_channel_status.update({
                    hostname: {
                        'portChannels': dict()
                    }
                })
                for po_name, po_status in d['show port-channel summary']['portChannels'].items():
                    port_channel_status[hostname]['portChannels'].update({
                        po_name: {
                            'linkState': 'up'
                        }
                    })
                    for eth_name, eth_status in po_status['ports'].items():
                        if 'PeerEthernet' not in eth_name:
                            port_channel_status[hostname]['portChannels'][po_name].update({
                                        'ports': {
                                            eth_name: {
                                                'lacpMisconfig': eth_status['lacpMisconfig'],
                                                'lagMember': eth_status['lagMember'],
                                                'linkDown': eth_status['linkDown'],
                                                'suspended': eth_status['suspended']
                                            }
                                        }
                                    })

    return port_channel_status


if __name__ == "__main__":
    eval_check_list = [  # list all functions allowed for eval() here
        'port_channel_status_from_dut',
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