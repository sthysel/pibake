import zipfile

import click
from psutil import disk_partitions


def get_mounted_candidates():
    """
    Returns list of mounted volumes that are likely to be sd-cards
    :return: list of sdiskpart named tuples
    """
    good = []
    for disk in disk_partitions():
        # filter out all /dev/sda* volumes
        if disk.device.find('/dev/sda') != -1:
            continue

        if disk.fstype == 'vfat' and disk.device.find('/dev/sdb') >= 0:
            good.append(disk)

    return good


def unzip_to_mount(image, mountpoint):
    click.echo('Baking image...')
    with zipfile.ZipFile(image, 'r') as zip_ref:
        zip_ref.extractall(mountpoint)
