# required imports and default settings
#from pybatfish.client.commands import *
#from pybatfish.client.extended import *
#from pybatfish.question import bfq, load_questions, list_questions
from pybatfish.exception import BatfishException
from pybatfish.datamodel.primitives import *
from pybatfish.datamodel.flow import HeaderConstraints, PathConstraints
from pybatfish.util import BfJsonEncoder
from pybatfish.datamodel.referencelibrary import *
from pybatfish.datamodel.referencelibrary import InterfaceGroup
from pybatfish.client.asserts import *

import logging
from attrdict import AttrDict
from netaddr import *
import json
import pandas as pd
import os
from pybfe.client.session import GRPCSession as Session

pd.set_option("display.width", 300)
pd.set_option("display.max_columns", 20)
pd.set_option("display.max_rows", None)
pd.set_option("display.max_colwidth", -1)

cert_path = "/users/samir/git/batfish-enterprise/proxy/intentionetCA.pem"
os.environ["REQUESTS_CA_BUNDLE"] = cert_path
os.environ["BFE_SSL_CERT"] = cert_path
host = "bfedev.local.intentionet.com"


try:
    bf = Session(host=host, ssl=True)
except:
    bf = Session.get('bf')

NETWORK = 'arista'
BASE_SNAPSHOT_DIR = '/Users/samir/git/arista-demo'
SNAPSHOT_NAME = 'snapshot0'
SNAPSHOT_DIR = f"{BASE_SNAPSHOT_DIR}/{SNAPSHOT_NAME}"

bf.set_network(NETWORK)
bf.init_snapshot(SNAPSHOT_DIR, name=SNAPSHOT_NAME, overwrite=True)

def exclude_vlan_loop_interface(interface):
    regex = "(^Vlan)|(^Loopback)"
    if re.search(regex, interface):
        return False
    else:
        return True


l3vni = bf.q.evpnL3VniProperties().answer().frame()
df = l3vni[l3vni.duplicated('Route_Distinguisher', keep=False)].sort_values('Route_Distinguisher')

ipOwn = bf.q.ipOwners(duplicatesOnly=True).answer().frame()

bgpPeer = bf.q.bgpPeerConfiguration().answer().frame()

bgpSess = bf.q.bgpSessionStatus().answer().frame()
bgpSess[bgpSess['Address_Families'].apply(lambda x: 'EVPN' in x)]

bgpComp = bf.q.bgpSessionCompatibility().answer().frame()
bgpComp[bgpComp['Address_Families'].apply(lambda x: 'EVPN' in x)]