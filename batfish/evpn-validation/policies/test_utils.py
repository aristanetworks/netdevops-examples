from pybfe.datamodel.policy import (
    STATUS_FAIL, STATUS_PASS
)

import os

def record_results(bf, status, message):

    session_type = os.environ.get('SESSION_TYPE')

    if session_type == 'bfe':
        if status == STATUS_PASS:
            bf.asserts._record_result(True, status=STATUS_PASS,
                                      message=message)
        elif status == STATUS_FAIL:
            bf.asserts._record_result(False, status=STATUS_FAIL,
                                      message=message)
        else:
            raise Exception

