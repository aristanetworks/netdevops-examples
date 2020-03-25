import netdiff
import sys

def from_csv_doc(in_data):
    # translate CSV topology doc into expected topology YAML

    fabric_topology_csv_row_list = in_data
    topology_dict = dict()
    for row in fabric_topology_csv_row_list:
        new_peer_entry = {
            row['Node Interface']: {
                'neighbor_port_name': row['Peer Interface'],
                'neighbor_hostname': row['Peer']
            }
        }
        if row['Node'] in topology_dict.keys():
            topology_dict[row['Node']].update(new_peer_entry)
        else:
            topology_dict.update({row['Node']: new_peer_entry})

    return topology_dict
    


if __name__ == "__main__":
    eval_check_list = [  # list all functions allowed for eval() here
        'from_csv_doc',
    ]
    args = netdiff.tools.parsers.src_dst_parser()
    in_data = netdiff.read._from(args.src_format, args.src_filename)
    if args.case in eval_check_list:
        out_data = eval(args.case + f'({in_data})')
        netdiff.write.to_file(args.dst_filename, args.dst_format, out_data)
    else:
        sys.exit(f'ERROR: Specified case {args.case} is not supported!')
