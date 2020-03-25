#!/usr/bin/env bash
# execute this script to build the data required for diff comparison from specified sources

set -o nounset  # exit script if uninitialised variable is used, same as set -u
set -o errexit  # exit script if statement returns non-true value, same as set -e

BASH_SCRIPT_DIRECTORY="$( cd "$(dirname "$0")" ; pwd -P )"
TESTS_DIRECTORY=$(dirname "${BASH_SCRIPT_DIRECTORY}")
POST_VALIDATION_REPOSITORY_DIRECTORY=$(dirname "${TESTS_DIRECTORY}")
NETDEVOPS_EXAMPLES_REPOSITORY_DIRECTORY=$(dirname "${POST_VALIDATION_REPOSITORY_DIRECTORY}")
INTENDED_DATA_DIR=${BASH_SCRIPT_DIRECTORY}/data/intended
IDD=${INTENDED_DATA_DIR}  # short name
CURRENT_DATA_DIR=${BASH_SCRIPT_DIRECTORY}/data/current_state
CDD=${CURRENT_DATA_DIR}  # short name

AVD_PYMOD=${POST_VALIDATION_REPOSITORY_DIRECTORY}/netdiff/env/avd  # AVD Python modules
PATH_TO_AVD=${NETDEVOPS_EXAMPLES_REPOSITORY_DIRECTORY}/ansible/avd-evpn-l3ls-1  # path to AVD test case data
# data structures required to build AVD data
DUT_STATE_YAML=${PATH_TO_AVD}/post_validation/state_outputs/duts_state.yaml
DUT_STATE_JSON=${PATH_TO_AVD}/post_validation/state_outputs/duts_state.json
TOPOLOGY_DOCUMENT=${PATH_TO_AVD}/documentation/DC1_FABRIC/DC1_FABRIC-topology.csv
STRUCTURED_CONFIGS_DIR=${PATH_TO_AVD}/intended/structured_configs

export PYTHONPATH=${POST_VALIDATION_REPOSITORY_DIRECTORY}  # for Python to find modules
export INTENDED_DATA_DIR  # used by some python modules
export CURRENT_DATA_DIR  # used by some python modules

######### BUILD INTENDED DATA ############
# build intended topology data
echo "-------- 1. Building Intended Data -----------------"
echo
echo "1.1 Building intended topology."
python3 ${AVD_PYMOD}/intended/topology.py -src=${TOPOLOGY_DOCUMENT} -dst=${INTENDED_DATA_DIR}/topology.yml -sfm csv -dfm yaml --case from_csv_doc
python3 ${AVD_PYMOD}/intended/topology.py -src=${TOPOLOGY_DOCUMENT} -dst=${INTENDED_DATA_DIR}/topology_no_server.yml -sfm csv -dfm yaml --case from_csv_doc_without_servers
python3 ${AVD_PYMOD}/intended/bgp.py -src=${STRUCTURED_CONFIGS_DIR} -dst=${INTENDED_DATA_DIR}/bgp_peering.yml -sfm string -dfm yaml --case from_struct_config
python3 ${AVD_PYMOD}/intended/environment.py -src=${TOPOLOGY_DOCUMENT} -dst=${INTENDED_DATA_DIR}/cpu_and_more.yml -sfm csv -dfm yaml --case cpu_from_csv_inventory
python3 ${AVD_PYMOD}/intended/port_status.py -src=${STRUCTURED_CONFIGS_DIR} -dst=${INTENDED_DATA_DIR}/port_status.yml -sfm string -dfm yaml --case port_channel_from_struct_cfg

######### BUILD CURRENT NETWORK STATE DATA ############
# build current topology data
echo "-------- 2. Building Current Data -----------------"
echo
echo "2.1 Building current topology."
python3 ${AVD_PYMOD}/current/topology.py -src=${DUT_STATE_JSON} -dst=${CURRENT_DATA_DIR}/topology.yml --src_format json --dst_format yaml --case from_dut
python3 ${AVD_PYMOD}/current/topology.py -src=${DUT_STATE_JSON} -dst=${CURRENT_DATA_DIR}/topology_no_server.yml --src_format json --dst_format yaml --case from_dut_no_localhost
python3 ${AVD_PYMOD}/current/bgp.py -src=${DUT_STATE_JSON} -dst=${CURRENT_DATA_DIR}/bgp_peering.yml --src_format json --dst_format yaml --case from_dut
python3 ${AVD_PYMOD}/current/environment.py -src=${DUT_STATE_JSON} -dst=${CURRENT_DATA_DIR}/cpu_and_more.yml --src_format json --dst_format yaml --case from_dut
python3 ${AVD_PYMOD}/current/port_status.py -src=${DUT_STATE_JSON} -dst=${CURRENT_DATA_DIR}/port_status.yml --src_format json --dst_format yaml --case port_channel_status_from_dut

######### RUN TESTS ############
echo "-------- 3. Run Tests -----------------"
echo
echo "3.1 Run Ward tests."
cd ${TESTS_DIRECTORY}/avd/ward
ward
# echo "3.1 Run PyTest tests."
# cd ${TESTS_DIRECTORY}/avd/pytest
# pytest -vv
