from translate.tools import *


def default(src_filename, dst_filename):
    # translate CSV topology doc into expected topology YAML

    fabric_topology_csv_row_list = read_from_csv(src_filename)
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

    write_yaml(dst_filename, topology_dict)


def no_server(src_filename, dst_filename):
    # translate CSV topology doc into expected topology YAML, except servers

    fabric_topology_csv_row_list = read_from_csv(src_filename)
    topology_dict = dict()
    for row in fabric_topology_csv_row_list:
        if 'server' not in row['Peer']:  # just for demo, find better way in prod
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

    write_yaml(dst_filename, topology_dict)
