import csv
import yaml
import json
import sys

def csv_file(csv_filename):
    # this file reads CSV and returns list of dictionaries
    row_list = list()
    header_row = list()
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for index, row in enumerate(csv_reader):
            if index == 0:
                header_row = row
            if index > 0:
                d = dict()
                for e_index, element in enumerate(row):
                    try:
                        key = header_row[e_index]
                    except Exception as _:
                        key = 'Column_number_{}'.format(e_index)
                    d.update({key: element})
                row_list.append(d)
    return row_list


def yaml_file(filename):
    with open(filename, mode='r') as f:
        yaml_data = yaml.load(f, Loader=yaml.FullLoader)
        return yaml_data


def json_file(filename):
    with open(filename, mode='r') as f:
        json_data = json.load(f)
        return json_data


def _from(in_format_name, in_filename):
    # this function will pick appropriate way to read the file base on format argument
    if in_format_name == 'json':
        in_data = json_file(in_filename)
    elif in_format_name == 'yaml':
        in_data = yaml_file(in_filename)
    elif in_format_name == 'csv':
        in_data = csv_file(in_filename)
    else:
        sys.exit(f'ERROR: {in_format_name} not yet supported')

    return in_data
