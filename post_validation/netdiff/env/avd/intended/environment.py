import netdiff
import sys


def cpu_from_csv_inventory(in_data):
    # defines expected CPU threshold for every switch in inventory
    platform_state_dict = dict()
    for row in in_data:
        if row['Node'] not in platform_state_dict.keys():
            platform_state_dict.update({
                row['Node']: {
                    'cpuInfo': {
                        'idle': {
                            '__comparison_mode': 'le',  # less or equal
                            '__ref_value': 71  # for demo only, normally should be significantly lower
                        }
                    }
                }
            })

    return platform_state_dict


if __name__ == "__main__":
    eval_check_list = [  # list all functions allowed for eval() here
        'cpu_from_csv_inventory',
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
