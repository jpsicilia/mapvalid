"""Smoke tests: the package installs and reports its version."""

import mapvalid


def test_version_is_a_non_empty_string():
    assert isinstance(mapvalid.__version__, str)
    assert mapvalid.__version__
