import netdiff
import sys

def port_channel_from_struct_cfg(structured_configs_dir):
    expected_port_channel_status = dict()
    struct_config_data = netdiff.read.yamls_from_dir(structured_configs_dir)
    for hostname, struct_config in struct_config_data.items():
        if isinstance(struct_config, dict):
            if 'port_channel_interfaces' in struct_config.keys():
                expected_port_channel_status.update({
                    hostname: {'portChannels': dict()},
                })
                for port_channel_name in struct_config['port_channel_interfaces'].keys():
                    expected_port_channel_status[hostname]['portChannels'].update({
                        port_channel_name: {
                            'linkState': 'up'
                        }
                    })
            if 'ethernet_interfaces' in struct_config.keys():
                for eth_name, eth_cfg in struct_config['ethernet_interfaces'].items():
                    if isinstance(eth_cfg, dict):
                        if 'channel_group' in eth_cfg.keys():
                            port_channel_name = 'Port-Channel{}'.format(eth_cfg['channel_group']['id'])
                            expected_port_channel_status[hostname]['portChannels'][port_channel_name].update({
                                'ports': {
                                    eth_name: {
                                        'lacpMisconfig': {'status': 'bundled'},
                                        'lagMember': True,
                                        'linkDown': False,
                                        'suspended': False
                                    }
                                }
                            })
    return expected_port_channel_status

if __name__ == "__main__":
    eval_check_list = [  # list all functions allowed for eval() here
        'port_channel_from_struct_cfg',
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
