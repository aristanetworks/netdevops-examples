import netdiff
import sys

def from_dut(in_data):

    platform_state_dict = dict()
    for hostname, details in in_data['duts'].items():
        platform_state_dict.update({
            hostname: {
                'cpuInfo': {
                    'idle': details['show processes top once']['cpuInfo']['%Cpu(s)']['idle']
                }
            }
        })

    return platform_state_dict

if __name__ == "__main__":
    eval_check_list = [  # list all functions allowed for eval() here
        'from_dut',
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
