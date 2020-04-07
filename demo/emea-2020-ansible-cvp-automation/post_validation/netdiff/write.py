import yaml
import sys

class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def yaml_file(dst_yaml_filename, data_to_write):
    with open(dst_yaml_filename, 'w') as file:
        yaml.SafeDumper = NoAliasDumper
        yaml.safe_dump(data_to_write, file, default_flow_style=False)

def to_file(dst_filename, format, data_to_write):
    if format == 'yaml':
        yaml_file(dst_filename, data_to_write)
    else:
        sys.exit(f'ERROR: The format specified ({format}) is not yet supported.')
