from pybfe.datamodel.policy import (
    STATUS_FAIL, STATUS_PASS
)

import os
from .test_utils import record_results

def test_l2_vni_flood_list(bf):
    os.environ['bf_policy_name'] = "VXLAN and EVPN Policies"
    bf.asserts.current_assertion = 'Assert no L2 VNIs have static flood lists'

    vni = bf.q.vxlanVniProperties().answer().frame()
    empty = vni[vni['VTEP_Flood_List'].str.len() != 0]

    try:
        assert len(empty)==0
        record_results(bf, status=STATUS_PASS, message='No L2 VNIs have static flood lists')
    except Exception as e:
        record_results(bf, status=STATUS_FAIL,
                                  message='L2 VNIs with static flood lists:\n{}'.format(empty))
        raise e


def test_evpn_bgp_sessions_correct(bf):
    os.environ['bf_policy_name'] = "VXLAN and EVPN Policies"
    bf.asserts.current_assertion = 'Assert all EVPN BGP sessions are properly configured'
    bgpComp = bf.q.bgpSessionCompatibility().answer().frame()
    df = bgpComp[(bgpComp['Address_Families'].apply(lambda x: 'EVPN' in x)) & (bgpComp['Configured_Status']!='UNIQUE_MATCH')]

    try:
        assert len(df)==0
        record_results(bf, status=STATUS_PASS, message='No EVPN BGP sessions are misconfigured')
    except Exception as e:
        record_results(bf, status=STATUS_FAIL,
                                  message='EVPN BGP sessions are misconfigured:\n{}'.format(df))
        raise e


def test_evpn_bgp_sessions_up(bf):
    os.environ['bf_policy_name'] = "VXLAN and EVPN Policies"
    bf.asserts.current_assertion = 'Assert all EVPN BGP sessions are established'
    bgpSess = bf.q.bgpSessionStatus().answer().frame()
    df = bgpSess[(bgpSess['Address_Families'].apply(lambda x: 'EVPN' in x)) & (bgpSess['Established_Status']!='ESTABLISHED')]

    try:
        assert len(df)==0
        record_results(bf, status=STATUS_PASS, message='All EVPN BGP sessions are established')
    except Exception as e:
        record_results(bf, status=STATUS_FAIL,
                                  message='EVPN BGP sessions are not established:\n{}'.format(df))
        raise e

def test_evpn_l3vni_rd_unique(bf):
    os.environ['bf_policy_name'] = "VXLAN and EVPN Policies"
    bf.asserts.current_assertion = 'Assert all L3 VNIs have unique RD'

    l3vni = bf.q.evpnL3VniProperties().answer().frame()
    df = l3vni[l3vni.duplicated('Route_Distinguisher', keep=False)].sort_values('Route_Distinguisher')

    try:
        assert len(df)==0
        record_results(bf, status=STATUS_PASS, message='All L3 VNIs have unique RD')
    except Exception as e:
        record_results(bf, status=STATUS_FAIL,
                                  message='L3 VNIs with the same RD:\n{}'.format(df))
        raise e
