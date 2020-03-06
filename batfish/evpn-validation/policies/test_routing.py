from pybfe.datamodel.policy import (
    STATUS_FAIL, STATUS_PASS
)

from netaddr import *
import os
import pytest

from .test_utils import record_results


def test_all_bgp_sessions_up(bf):
    os.environ['bf_policy_name'] = "Routing and Routing Protocol Policies"
    bf.asserts.assert_no_unestablished_bgp_sessions()

def test_no_fabric_ibgp_sessions(bf):
    os.environ['bf_policy_name'] = "Routing and Routing Protocol Policies"
    bf.asserts.current_assertion = 'Assert no iBGP sessions configured in the fabric'

    fabric_nodes = "/tg.*/"
    ibgp_sessions = bf.q.bgpSessionCompatibility(nodes=fabric_nodes, type='/IBGP.*/').answer().frame()[['Node', 'VRF', 'Local_AS', 'Remote_Node', 'Remote_AS']]

    try:
        assert len(ibgp_sessions.index)==0
        record_results(bf, status=STATUS_PASS, message='All routers only have eBGP sessions')
    except Exception as e:
        record_results(bf, status=STATUS_FAIL,
                                  message='Routers with iBGP sessions:\n{}'.format(ibgp_sessions))
        raise e

def test_no_forwarding_loops(bf):
    os.environ['bf_policy_name'] = "Routing and Routing Protocol Policies"
    bf.asserts.assert_no_forwarding_loops()

def test_all_leaf_have_route_for_all_host_subnets(bf):
    os.environ['bf_policy_name'] = "Routing and Routing Protocol Policies"
    bf.asserts.current_assertion = 'Assert all leaf routers have routes to host subnets'

    # get ipAddress for all VLAN interfaces on all leaf routers
    tip = bf.q.ipOwners().answer().frame()
    leaf_tip = tip[(tip['Node'].str.contains('leaf'))]
    leaf_vlan_tip = tip[(tip['Node'].str.contains('leaf')) & (tip['Interface'].str.contains('vlan'))]

    # convert to subnet
    subnet = []
    for vlan in leaf_vlan_tip.itertuples():
        t_net = "{}/{}".format(vlan.IP, vlan.Mask)
        z = IPNetwork(t_net)
        subnet.append(str(z.cidr))

    # get list of leaf routers in snapshot and get routes for default VRF for all leaf routers
    leaf_list = list(bf.q.nodeProperties(nodes="/leaf.*/", properties='Hostname').answer().frame()['Node'])
    leaf_routes = bf.q.routes(nodes='/leaf.*/', vrfs='default').answer().frame()

    # identify leaf routers that are missing subnets for VLAN interfaces
    missing_leaf = []
    for leaf in leaf_list:
        t_routes = set(leaf_routes[leaf_routes['Node'] == leaf]['Network'])
        t_list = [item for item in set(subnet) if item not in t_routes]
        if len(t_list) != 0:
            missing_leaf.append(leaf)
            print(leaf)

    try:
        assert len(missing_leaf)==0
        record_results(bf, status=STATUS_PASS, message='All host subnets are present on all leaf routers')
    except Exception as e:
        record_results(bf, status=STATUS_FAIL,
                                  message='{} are missing some host subnets'.format(missing_leaf))
        raise e

def test_no_duplicate_router_ids(bf):
    os.environ['bf_policy_name'] = "Routing and Routing Protocol Policies"
    bf.asserts.current_assertion = 'Assert all routers have an unique router-id'

    bgpProc = bf.q.bgpProcessConfiguration(properties='/^Route.*/').answer().frame()
    rtr_id_map = bgpProc[bgpProc['VRF']=='default'][['Node', 'Router_ID']]

    dup_rtr_id_df = rtr_id_map[rtr_id_map.duplicated(['Router_ID'], keep=False)]

    try:
        assert len(dup_rtr_id_df.index)==0
        record_results(bf, status=STATUS_PASS, message='All routers have a unique router-id')
    except Exception as e:
        record_results(bf, status=STATUS_FAIL,
                                  message='Routers with duplicate router-ids:\n{}'.format(dup_rtr_id_df))
        raise e

def test_leaf_spine_bgp_peers(bf):
    os.environ['bf_policy_name'] = "Routing and Routing Protocol Policies"
    bf.asserts.current_assertion = 'Assert all leaf routers have configured BGP session for all spine routers'

    num_spines = 4
    bad_leaf = []
    bgpPeer = bf.q.bgpPeerConfiguration(nodes='/leaf.*/', properties='/Local_IP/').answer().frame()
    nodes_list = set(bgpPeer['Node'])

    for node in nodes_list:
        if len(bgpPeer[bgpPeer['Node']==node]) != num_spines:
            bad_leaf.append(node)

    try:
        assert len(bad_leaf)==0
        record_results(bf, status=STATUS_PASS, message='All leaf routers have BGP sessions configured for each spine')
    except Exception as e:
        record_results(bf, status=STATUS_FAIL,
                                  message='Leaf routers that do not have configred BGP sessions to ALL spines:\n{}'.format(bad_leaf))
        raise e