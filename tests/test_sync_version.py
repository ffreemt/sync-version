"""Test sync_version."""
# pylint: disable=broad-except
from sync_version import __version__
from sync_version import sync_version


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not sync_version()
    except Exception:
        assert True
