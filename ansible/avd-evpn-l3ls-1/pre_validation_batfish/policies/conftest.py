import logging
import os
import pandas as pd
import pytest
from pybatfish.client.session import Session
import uuid

def pandas_init():
    """Customize pandas table output."""
    pd.set_option("display.width", 300)
    pd.set_option("display.max_columns", 20)
    pd.set_option("display.max_rows", 1000)
    pd.set_option("display.max_colwidth", -1)


def pytest_addoption(parser):
    """Adds custom options to pytest for snapshot and network name"""
    parser.addoption("--snapshot", action="store",
                     help="Name of snapshot")
    parser.addoption("--network", action="store",
                    help="Name of network")


@pytest.fixture(scope="session")
def snapshot_name(request):
    name = request.config.getoption("--snapshot")
    if name is None:
        raise ValueError(
            "Snapshot name is required. Please pass '--snapshot' argument")
    return name

@pytest.fixture(scope="session")
def network_name(request):
    name = request.config.getoption("--network")
    if name is None:
        raise ValueError(
            "Network name is required. Please pass '--network' argument")

    return name

@pytest.fixture(scope="session")
def bf(network_name, snapshot_name):
    """Batfish session fixture"""

    try:
        bf = Session.get('bfe')
        os.environ["SESSION_TYPE"] = 'bfe'
    except:
        bf = Session.get('bf')
        os.environ["SESSION_TYPE"] = 'bf'

    bf.enable_diagnostics = False
    bf.set_network(network_name)
    bf.set_snapshot(snapshot_name)
    return bf


p_id = uuid.uuid4().hex

def pytest_sessionstart(session):
    os.environ['bf_policy_name'] = session.name

def pytest_runtest_setup(item):
    # Get test file name
    test_file_name = os.path.basename(item.parent.name)
    test_name = item.name
    os.environ['bf_policy_name'] = test_file_name
    os.environ['bf_policy_id'] = p_id
    os.environ['bf_test_name'] = test_name

# Customize logging and pandas
logging.getLogger('pybatfish').setLevel(logging.WARN)
pandas_init()


