
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

from ward import test, xfail
import netdiff

@test("Verify if Ward is working and can assert True")
def test_can_assert_true():
    # before any test verify if PyTest is working and can assert True
    assert True

@test("Verify if topology is correct")  # based on 'lldp neighbors'
def test_if_topology_is_correct(filename='topology.yml'):
    current_data_aka_left, intended_data_aka_right = netdiff.process.test_data.for_yaml_diff(filename)
    assert current_data_aka_left == intended_data_aka_right

@test("Verify if topology is correct, without servers")  # based on 'lldp neighbors'
def test_if_topology_is_correct_without_servers(filename='topology_no_server.yml'):
    current_data_aka_left, intended_data_aka_right = netdiff.process.test_data.for_yaml_diff(filename)
    assert current_data_aka_left == intended_data_aka_right

@test("Verify if BGP peering is correct")
def test_if_bgp_peering_is_correct(filename='bgp_peering.yml'):
    current_data_aka_left, intended_data_aka_right = netdiff.process.test_data.for_yaml_diff(filename)
    assert current_data_aka_left == intended_data_aka_right

# @xfail("This is expected to fail as threshold is too high.")  # <<<---<<< can be enabled during the demo
@test("Verify CPU Utilization")
def test_cpu_utilization(filename='cpu_and_more.yml'):
    current_data_aka_left, intended_data_aka_right = netdiff.process.test_data.for_yaml_diff(filename)
    assert current_data_aka_left == intended_data_aka_right

@test("Port-channel status check")
def test_port_channel_status(filename='port_status.yml'):
    current_data_aka_left, intended_data_aka_right = netdiff.process.test_data.for_yaml_diff(filename)
    assert current_data_aka_left == intended_data_aka_right

@test("MLAG status check")
def test_mlag_status(filename='mlag.yml'):
    current_data_aka_left, intended_data_aka_right = netdiff.process.test_data.for_yaml_diff(filename)
    assert current_data_aka_left == intended_data_aka_right
