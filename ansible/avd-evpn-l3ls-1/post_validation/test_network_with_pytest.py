#!/usr/bin/env python3

#
# Copyright (c) 2019, Arista Networks, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#   Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
#
#   Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
#
#   Neither the name of Arista Networks nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# 'AS IS' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL ARISTA NETWORKS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
# IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

__author__ = 'Petr Ankudinov'

import pytest
import yaml
import json
import os
from io import StringIO

test_input_data_dir = './test_input_data'
expected_data_dir = './expected_data'


def load_yaml(filename):
    try:
        file = open(filename, mode='r')
        yaml_data = yaml.load(file, Loader=yaml.FullLoader)
        file.close()
    except Exception as _:
        return False
    else:
        return yaml_data


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def get_realpath(filename, parent_dir=''):

    parent_dir_realpath = ''
    try:
        parent_dir_realpath = os.path.realpath(parent_dir)
    except Exception as _:
        pass  # ignore exception

    if parent_dir_realpath:
        realpath = os.path.join(parent_dir_realpath, filename)
    else:
        script_realpath = os.path.realpath(__file__)
        script_dir = os.path.dirname(script_realpath)
        if os.path.isdir(os.path.join(script_dir, parent_dir)):
            realpath = os.path.join(
                os.path.join(script_dir, parent_dir), filename
            )
        elif os.path.isdir(os.path.dirname(filename)):
            realpath = filename
        else:
            realpath = os.path.join(script_dir, filename)

    return realpath


def delete_non_unique_elements(test_json, expected_json):
    # this function removes elements that are present in both dictionaries
    # it's non-recursive and currently walks over top keys only
    # that makes diff easier to read, but is not ideal and better solution may be required in future
    try:
        if isinstance(test_json, dict) and isinstance(expected_json, dict):
            for key in test_json.copy().keys():
                if key in expected_json.keys():
                    if json.dumps(test_json[key], sort_keys=True) == json.dumps(expected_json[key], sort_keys=True):
                        del (test_json[key])
                        del (expected_json[key])
        return test_json, expected_json
    except Exception as _:
        return False, False


def load_and_pre_process(filename_prefix):

    try:

        yaml_filename = filename_prefix + '.yml'

        test_yaml_realpath = get_realpath(yaml_filename, test_input_data_dir)
        expected_yaml_realpath = get_realpath(yaml_filename, expected_data_dir)
        test_input_json = load_yaml(test_yaml_realpath)
        expected_json = load_yaml(expected_yaml_realpath)

        # remove common data, optional for compact diff
        unique_test_json, unique_expected_json = delete_non_unique_elements(test_input_json, expected_json)

        # convert back to YAML
        test_stream = StringIO()
        expected_stream = StringIO()
        yaml.SafeDumper = NoAliasDumper
        yaml.safe_dump(unique_test_json, test_stream, default_flow_style=False)
        yaml.safe_dump(unique_expected_json, expected_stream, default_flow_style=False)

        return test_stream.getvalue(), expected_stream.getvalue()

    except Exception as _:
        return False, False


def test_can_assert_true():
    # before any test verify if PyTest is working and can assert True
    assert True


# @pytest.mark.parametrize("filename_prefix", ['topology'])
# def test_if_topology_is_correct(filename_prefix):
#     test_data_aka_left, expected_data_aka_right = load_and_pre_process(filename_prefix)

#     assert test_data_aka_left == expected_data_aka_right


@pytest.mark.parametrize("filename_prefix", ['topology_no_server'])
def test_if_topology_is_correct_without_servers(filename_prefix):
    test_data_aka_left, expected_data_aka_right = load_and_pre_process(filename_prefix)

    assert test_data_aka_left == expected_data_aka_right


@pytest.mark.parametrize("filename_prefix", ['bgp_peering'])
def test_if_bgp_peering_is_correct(filename_prefix):
    test_data_aka_left, expected_data_aka_right = load_and_pre_process(filename_prefix)

    assert test_data_aka_left == expected_data_aka_right
