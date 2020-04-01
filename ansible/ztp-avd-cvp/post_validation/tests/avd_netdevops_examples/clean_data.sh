#!/usr/bin/env bash
# execute this script to clean test data

set -o nounset  # exit script if uninitialised variable is used, same as set -u
set -o errexit  # exit script if statement returns non-true value, same as set -e

BASH_SCRIPT_DIRECTORY="$( cd "$(dirname "$0")" ; pwd -P )"
TESTS_DIRECTORY=$(dirname "${BASH_SCRIPT_DIRECTORY}")
REPOSITORY_DIRECTORY=$(dirname "${TESTS_DIRECTORY}")
INTENDED_DATA_DIR=${BASH_SCRIPT_DIRECTORY}/data/intended
IDD=${INTENDED_DATA_DIR}  # short name
CURRENT_DATA_DIR=${BASH_SCRIPT_DIRECTORY}/data/current_state
CDD=${CURRENT_DATA_DIR}  # short name

# delete test data
rm -f ${INTENDED_DATA_DIR}/*
rm -f ${CURRENT_DATA_DIR}/*