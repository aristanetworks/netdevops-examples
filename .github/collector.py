#!/usr/bin/python
# coding: utf-8 -*-

#
# GNU General Public License v3.0+
#
# Copyright 2020 TiTom73
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: //www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import sys
import requests
from jinja2 import Environment, FileSystemLoader

GH_API_ENDPOINT = 'https://api.github.com/users/arista-netdevops-community/repos'
JSON_FIELDS = { 'name':'project_name', 'description':'description', 'html_url':'homepage', 'updated_at': 'last_commit'}
TEMPLATE_MARKDOWN = 'page.md.j2'
OUTPUT_FILE = '../docs/index.md'

def get_gh_api(url):
    """
    get_gh_api Extract information using GET

    Collect Github data from their public API
    Current version does not support authentication

    Parameters
    ----------
    url : string
        Github API string to get.

    Returns
    -------
    json
        Response from GH.
    """
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        return response.json()
    return {}

def extract_fields(gh_json, fields):
    """
    extract_fields Extract field from GH API data

    Extract fields from GH API data and standardize name of keys

    Parameters
    ----------
    gh_json : json
        JSON content from Github
    fields : dict
        A list of fields to extract and the name we want to use as standard.
    """
    data = list()
    for entry in gh_json:
        cell = dict()
        for field in fields:
            cell[fields[field]] = entry[field]
        data.append(cell)
    return data


if __name__ == '__main__':
    data = get_gh_api(url=GH_API_ENDPOINT)
    projects = extract_fields(gh_json=data, fields=JSON_FIELDS)
    root = os.path.dirname(os.path.abspath(__file__))
    env = Environment( loader = FileSystemLoader(root) )
    env.trim_blocks = True
    env.lstrip_blocks = True
    env.rstrip_blocks = True
    template = env.get_template(TEMPLATE_MARKDOWN)
    output = template.render(projects=projects)
    filename = os.path.join(root, OUTPUT_FILE)
    with open(filename, 'w') as fh:
        fh.write(output)

    sys.exit(0)