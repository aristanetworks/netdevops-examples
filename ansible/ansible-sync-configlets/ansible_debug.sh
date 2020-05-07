#!/bin/sh

echo 'Configure module for logging:'
echo '  - Logging Level: debug'
echo '  - Logging File: arista.cvp.debug.log'
echo '  - URL Lib logging: warning'

export ANSIBLE_CVP_LOG_FILE=arista.cvp.debug.log
export ANSIBLE_CVP_LOG_LEVEL=debug
export ANSIBLE_CVP_LOG_APICALL=warning
