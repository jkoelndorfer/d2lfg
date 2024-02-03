"""
d2lfg global test configuration
===============================

This file contains global pytest configuration for d2lfg.
"""

import pytest

from tests.testhelper.typing import FixtureRequest, PathTyper


@pytest.fixture(params=[lambda p: str(p), lambda p: p])
def pathtyper(request: FixtureRequest[PathTyper]) -> PathTyper:
    return request.param
