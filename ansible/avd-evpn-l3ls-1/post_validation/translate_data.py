#!/usr/bin/env python3

# This script will take convert intended config data and data collected from DUTs into a diff-comparable YAML format.

from translate.tools import *

# translate_data.py requires some configuration to find files to be translated.
config_yaml_filename = './translate_data_cfg.yml'

run_translation(config_yaml_filename)
