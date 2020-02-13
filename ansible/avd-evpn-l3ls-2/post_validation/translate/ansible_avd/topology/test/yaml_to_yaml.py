from translate.tools import *


def dut_lldp(src_filename, dst_filename):
    # translate test data from YAML with show commands into test topology YAML

    dut_show_data = load_yaml(src_filename)

    topology_dict = dict()
    for hostname, details in dut_show_data['duts'].items():
        for peer in details['show lldp neighbors']['lldpNeighbors']:
            new_peer_entry = {
                peer['port']: {
                    'neighbor_port_name': peer['neighborPort'],
                    'neighbor_hostname': peer['neighborDevice']
                }
            }
            if hostname in topology_dict.keys():
                topology_dict[hostname].update(new_peer_entry)
            else:
                topology_dict.update({hostname: new_peer_entry})

    write_yaml(dst_filename, topology_dict)


def dut_lldp_no_localhost(src_filename, dst_filename):
    # translate test data from YAML with show commands into test topology YAML

    dut_show_data = load_yaml(src_filename)

    topology_dict = dict()
    for hostname, details in dut_show_data['duts'].items():
        for peer in details['show lldp neighbors']['lldpNeighbors']:
            if 'localhost' not in peer['neighborDevice']:  # just for demo, find better way in prod
                new_peer_entry = {
                    peer['port']: {
                        'neighbor_port_name': peer['neighborPort'],
                        'neighbor_hostname': peer['neighborDevice']
                    }
                }
                if hostname in topology_dict.keys():
                    topology_dict[hostname].update(new_peer_entry)
                else:
                    topology_dict.update({hostname: new_peer_entry})

    write_yaml(dst_filename, topology_dict)
