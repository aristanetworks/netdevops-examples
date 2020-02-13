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

# various tools to support data translation

import yaml
import sys
import csv
import os
from time import time as time
from datetime import datetime as datetime
import translate  # this one is used by eval()


def load_yaml(filename, ignore_error=False, debug=True):
    if debug:  # to debug load time for big YAMLs
        print('Loading %s started at: ' % filename, time_stamp())
    try:
        file = open(filename, mode='r')
    except Exception as _:
        if ignore_error:
            pass
        else:
            sys.exit('Can not open %s\nERROR: %s' % (filename, _))
    else:
        try:
            yaml_data = yaml.load(file, Loader=yaml.FullLoader)
            file.close()
        except Exception as _:
            return False
        else:
            if debug:  # to debug load time for big YAMLs
                print('%s was loaded successfully at: ' % filename, time_stamp())
            return yaml_data


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def write_yaml(filename, d):
    try:
        with open(filename, 'w') as file:
            yaml.SafeDumper = NoAliasDumper
            yaml.safe_dump(d, file, default_flow_style=False)
    except Exception as _:
        sys.exit('Can not create %s\nERROR: %s' % (filename, _))


def time_stamp():
    """
    time_stamp function can be used for debugging or to display timestamp for specific event to a user
    :return: returns current system time as a string in Y-M-D H-M-S format
    """
    time_not_formatted = time()
    time_formatted = datetime.fromtimestamp(time_not_formatted).strftime('%Y-%m-%d:%H:%M:%S.%f')
    return time_formatted


def get_realpath(file_or_dir_name, parent_dir=''):

    if os.path.isdir(file_or_dir_name) or os.path.isdir(os.path.dirname(file_or_dir_name)):
        return file_or_dir_name

    else:

        parent_dir_realpath = ''
        try:
            parent_dir_realpath = os.path.realpath(parent_dir)
        except Exception as _:
            pass  # ignore exception

        if parent_dir_realpath:
            realpath = os.path.join(parent_dir_realpath, file_or_dir_name)
        else:
            script_realpath = os.path.realpath(__file__)
            script_dir = os.path.dirname(script_realpath)
            if os.path.isdir(os.path.join(script_dir, parent_dir)):
                realpath = os.path.join(
                    os.path.join(script_dir, parent_dir), file_or_dir_name
                )
            else:
                realpath = os.path.join(script_dir, file_or_dir_name)

        return realpath


def read_from_csv(csv_filename):
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


def run_translation(cfg_yaml_filename):
    cfg = load_yaml(cfg_yaml_filename)['translate_data_config']

    expected_src_prefix = ''
    expected_dst_prefix = ''
    test_src_prefix = ''
    test_dst_prefix = ''

    # if location prefix was changed, use new prefix for later cases
    for translate_case in cfg['translate_cases']:
        if 'expected_src_prefix' in translate_case.keys():
            expected_src_prefix = translate_case['expected_src_prefix']
        if 'expected_dst_prefix' in translate_case.keys():
            expected_dst_prefix = translate_case['expected_dst_prefix']
        if 'test_src_prefix' in translate_case.keys():
            test_src_prefix = translate_case['test_src_prefix']
        if 'test_dst_prefix' in translate_case.keys():
            test_dst_prefix = translate_case['test_dst_prefix']
        if 'mode' in translate_case.keys():
            mode = translate_case['mode']
            if 'expected' in mode:
                src_filename = get_realpath(translate_case['src'], expected_src_prefix)  # used by eval()
                dst_filename = get_realpath(translate_case['dst'], expected_dst_prefix)  # used by eval()
            else:
                src_filename = get_realpath(translate_case['src'], test_src_prefix)  # used by eval()
                dst_filename = get_realpath(translate_case['dst'], test_dst_prefix)  # used by eval()

            # run the translation case
            if mode.startswith('translate/'):  # simple way to keep eval() safe
                eval(mode.replace('/', '.') + '(src_filename, dst_filename)')
