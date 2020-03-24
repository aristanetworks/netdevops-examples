#!/usr/bin/env bash
# execute this script to build the data required for diff comparison from specified sources

set -o nounset  # exit script if uninitialised variable is used, same as set -u
set -o errexit  # exit script if statement returns non-true value, same as set -e

BASH_SCRIPT_DIRECTORY="$( cd "$(dirname "$0")" ; pwd -P )"
TESTS_DIRECTORY=$(dirname "${BASH_SCRIPT_DIRECTORY}")
REPOSITORY_DIRECTORY=$(dirname "${TESTS_DIRECTORY}")
INTENDED_DATA_DIR=${BASH_SCRIPT_DIRECTORY}/data/intended
IDD=${INTENDED_DATA_DIR}  # short name
CURRENT_DATA_DIR=${BASH_SCRIPT_DIRECTORY}/data/current_state
CDD=${CURRENT_DATA_DIR}  # short name

AVD_PYMOD=${REPOSITORY_DIRECTORY}/netdiff/env/avd  # AVD Python modules
PATH_TO_AVD=~/PycharmProjects/ansible-avd-testing/nashua-lab/test-case-1  # path to AVD test case data
# data structures required to build AVD data
DUT_STATE_YAML=${PATH_TO_AVD}/fabric_validation/state_outputs/duts_state.yaml
DUT_STATE_JSON=${PATH_TO_AVD}/fabric_validation/state_outputs/duts_state.json
TOPOLOGY_DOCUMENT=${PATH_TO_AVD}/documentation/DC1_FABRIC/DC1_FABRIC-topology.csv

export PYTHONPATH=${REPOSITORY_DIRECTORY}  # for Python to find modules
export INTENDED_DATA_DIR  # used by some python modules
export CURRENT_DATA_DIR  # used by some python modules

######### BUILD INTENDED DATA ############
# build intended topology data
echo "-------- 1. Building Intended Data -----------------"
echo
echo "1.1 Building intended topology."
python3 ${AVD_PYMOD}/intended/topology.py -src=${TOPOLOGY_DOCUMENT} -dst=${INTENDED_DATA_DIR}/topology.yml --src_format csv --dst_format yaml


######### BUILD CURRENT NETWORK STATE DATA ############
# build current topology data
echo "-------- 2. Building Current Data -----------------"
echo
echo "2.1 Building current topology."
# python3 ${AVD_PYMOD}/current/topology.py -src=${DUT_STATE_YAML} -dst=${CURRENT_DATA_DIR}/topology.yml --src_format yaml --dst_format yaml

######### RUN TESTS ############
echo "-------- 3. Run Tests -----------------"
echo
echo "3.1 Run Ward tests."
cd ${TESTS_DIRECTORY}/avd/ward
ward
# echo "3.1 Run Ward tests."
# cd ${TESTS_DIRECTORY}/avd/pytest
# pytest -vv
