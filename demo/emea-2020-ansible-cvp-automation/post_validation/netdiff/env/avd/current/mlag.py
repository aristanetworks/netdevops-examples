import netdiff
import sys


def mlag_status_from_dut(in_data):

    mlag_status_dict = dict()

    for hostname, d in in_data['duts'].items():

        mlag = d['show mlag detail']
        if 'domainId' in mlag.keys():
            try:
                mlag_status_dict.update({
                    hostname: {
                        'configSanity': mlag['configSanity'],
                        'detail': {
                            'mlagPorts': {
                                'Inactive': mlag['mlagPorts']['Inactive'],
                                'Active-partial': mlag['mlagPorts']['Active-partial'],
                                'Disabled': mlag['mlagPorts']['Disabled']
                            },
                            'negStatus': mlag['negStatus'],
                            'peerLinkStatus': mlag['peerLinkStatus'],
                            'portsErrdisabled': mlag['portsErrdisabled'],
                            'state': mlag['state']
                        }
                    }
                })
            except Exception as _:
                pass

    return mlag_status_dict


if __name__ == "__main__":
    eval_check_list = [  # list all functions allowed for eval() here
        'mlag_status_from_dut',
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