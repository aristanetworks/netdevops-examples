import os

try:
    from pybfe.datamodel.policy import (
        STATUS_FAIL, STATUS_PASS
    )
    TEST_STATUS_FAIL = STATUS_FAIL
    TEST_STATUS_PASS = STATUS_PASS
except:
    TEST_STATUS_PASS = u"Pass"
    TEST_STATUS_FAIL = u"Fail"


def record_results(bf, assertion, pass_message, fail_message):

    session_type = os.environ.get('SESSION_TYPE')

    try:
        assert(assertion)
        if session_type == 'bfe':
            bf.asserts._record_result(True, status=STATUS_PASS,
                                      message=pass_message)
    except Exception as e:
        if session_type == 'bfe':
            bf.asserts._record_result(False, status=STATUS_FAIL,
                                      message=fail_message)
        raise AssertionError(fail_message)
