import os
import netdiff
import re
from jsonpath2 import Path
import json
from io import StringIO
import yaml


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def jp2_query(json_to_query, query_expression):
    jp2_expr = Path.parse_str(query_expression)
    value_list = list()
    node_jsonpath_list = list()
    for m in jp2_expr.match(json_to_query):
        value_list.append(m.current_value)
        node_jsonpath_list.append(m.node.tojsonpath())
    return value_list, node_jsonpath_list


def build_key_list_from_jsonpath(json_path_to_node):
    key_list = list()
    for key in re.split(r"[\[\]$]", json_path_to_node):
        if key:
            if ('"' in key) or ("'" in key):
                key_list.append(str(re.sub("['\"]", '', key)))
            else:
                key_list.append(int(key))

    return key_list


def delete_non_unique_elements(test_json, expected_json):
    # this function removes elements that are present in both dictionaries
    # it's non-recursive and currently walks over top keys only
    # that makes diff easier to read, but is not ideal and better solution may be required in future
    if isinstance(test_json, dict) and isinstance(expected_json, dict):
        for key in test_json.copy().keys():
            if key in expected_json.keys():
                if json.dumps(test_json[key], sort_keys=True) == json.dumps(expected_json[key], sort_keys=True):
                    del (test_json[key])
                    del (expected_json[key])
    return test_json, expected_json


def run_comparison(test_json, expected_json):
    val_list, jp_list = jp2_query(expected_json, '$..__comparison_mode')
    if val_list:
        for index, comparison_mode in enumerate(val_list):
            ref_value = expected_json
            dut_value = test_json
            val_key_list = build_key_list_from_jsonpath(jp_list[index])[:-1]
            parent_obj_key_list = build_key_list_from_jsonpath(jp_list[index])[:-1]
            # print(parent_obj_key_list)
            for key in val_key_list:
                ref_value = ref_value[key]
                dut_value = dut_value[key]
            if comparison_mode == 'ge':
                if dut_value > ref_value['__ref_value']:  # exclude all elements not matching condition
                    exp = expected_json
                    tst = test_json
                    for k in parent_obj_key_list[:-1]:
                        exp = exp[k]
                        tst = tst[k]
                    exp[parent_obj_key_list[-1]] = dut_value
                    tst[parent_obj_key_list[-1]] = dut_value
                else:
                    exp = expected_json
                    for k in parent_obj_key_list[:-1]:
                        exp = exp[k]
                    exp[parent_obj_key_list[-1]] = 'expected value >= {}'.format(ref_value['__ref_value'])

    return test_json, expected_json


def json_to_yaml_string(json_data):
    data_stream = StringIO()
    yaml.SafeDumper = NoAliasDumper
    yaml.safe_dump(json_data, data_stream, default_flow_style=False)
    return data_stream.getvalue()

def for_yaml_diff(filename):
    indended_data_file = os.path.join(os.environ['INTENDED_DATA_DIR'], filename)
    current_data_file = os.path.join(os.environ['CURRENT_DATA_DIR'], filename)

    intended_data = netdiff.read.yaml_file(indended_data_file)
    current_data = netdiff.read.yaml_file(current_data_file)

    # remove common data, optional for compact diff
    current_data, intended_data = delete_non_unique_elements(current_data, intended_data)
    current_data, intended_data = run_comparison(current_data, intended_data)


    current_data_yaml = json_to_yaml_string(current_data)
    intended_data_yaml = json_to_yaml_string(intended_data)
    return current_data_yaml, intended_data_yaml
