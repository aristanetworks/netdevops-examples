import netdiff
import sys

def from_struct_config(structured_configs_dir):

    mlag_state_dict = dict()
    struct_config_data = netdiff.read.yamls_from_dir(structured_configs_dir)
    for hostname, struct_config in struct_config_data.items():
        if isinstance(struct_config, dict):
            if 'leaf_mlag' in struct_config.keys():
                if struct_config['leaf_mlag']:
                    mlag_state_dict.update({
                        hostname: {
                            'configSanity': 'consistent',
                            'detail': {
                                'mlagPorts': {
                                    'Inactive': 0
                                },
                                'negStatus': 'connected',
                                'peerLinkStatus': 'up',
                                'portsErrdisabled': False,
                                'state': 'active'
                            }
                        }
                    })

    return mlag_state_dict


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
