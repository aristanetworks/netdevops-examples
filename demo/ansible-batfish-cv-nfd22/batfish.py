from pybatfish.client.commands import *
from pybatfish.question.question import load_questions, list_questions
from pybatfish.question import bfq
from pybatfish.datamodel.flow import *

load_questions()
CURRENT_SNAPSHOT_NAME = "current"
CURRENT_SNAPSHOT_PATH = "tmp/current"
CANDIDATE1_SNAPSHOT_NAME = "candidate"
CANDIDATE1_SNAPSHOT_PATH = "tmp/candidate"


bf_set_network("network-filters")
bf_init_snapshot(CURRENT_SNAPSHOT_PATH, name=CURRENT_SNAPSHOT_NAME, overwrite=True)
bf_init_snapshot(CANDIDATE1_SNAPSHOT_PATH, name=CANDIDATE1_SNAPSHOT_NAME, overwrite=True)

node_name = "cs-lf12"
filter_name = "demo"

# Traffic going to a blacklisted IP address
traffic1 = HeaderConstraints(srcIps="192.168.2.0/24",
                            dstIps="158.174.122.199",
                            ipProtocols=["tcp"],
                            dstPorts="80,8080")
# Traffic that should be allowed to external IP
traffic2 = HeaderConstraints(srcIps="192.168.2.0/24",
                            dstIps="158.175.122.199",
                            ipProtocols=["tcp"],
                            dstPorts="80,8080")
currentblacklist = bfq.searchFilters(headers=traffic1,
                           filters=filter_name,
                           # nodes=node_name,
                           action="permit").answer(
                               snapshot=CURRENT_SNAPSHOT_NAME
                           )
# No output indicates the traffic was permitted, i.e. find flows that match this search

# print("Is traffic allowed to go to blacklisted ip?")
# print(currentblacklist.frame())
# print(currentblacklist.frame().size)

# testing the opposite case.. here we see that there is no traffic permitted that 
# isn't destined for those two hosts

# print("Is traffic allowed to go to whitelisted ip?")
# currentpermit = bfq.searchFilters(headers=traffic2,
#                            filters=filter_name,
#                            nodes=node_name,
#                            action="deny").answer(
#                                snapshot=CURRENT_SNAPSHOT_NAME
#                            )
# print(currentpermit.frame())
# print(currentpermit.frame().size)
# pybatfish.client.asserts.assert_filter_denies(filters, headers, startLocation=None, soft=False, snapshot=None, session=None, df_format='table')

answer2 = bfq.searchFilters(headers=traffic1,
                           filters=filter_name,
                           # nodes=node_name,
                           action="permit").answer(
                               snapshot=CANDIDATE1_SNAPSHOT_NAME
                           )
print ("Will Candidate config block blacklisted ip?")
print(answer2.frame())
print(answer2.frame().size)
# No output indicates the traffic was permitted, i.e. find flows that match this search
answer3 = bfq.searchFilters(headers=traffic2,
                           filters=filter_name,
                           # nodes=node_name,
                           action="deny").answer(
                               snapshot=CANDIDATE1_SNAPSHOT_NAME
                           )
print ("Will Candidate config allow whitelisted ip?")
print(answer3.frame())
print(answer3.frame().size)
if (answer3.frame().size > 0):
  raise SystemExit('Whitelisted ip address has been blocked')
