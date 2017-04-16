from unittest.mock import patch

from pibake.disks import get_mounted_candidates


@patch('pibake.disks.disk_partitions')
def test_get_mounted_candidates():
    assert get_mounted_candidates() == ('/dev/sdb1 mounted', '/run/media/thys/A881-FFA5')
