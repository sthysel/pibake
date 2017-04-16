import os
import sys

import click
import requests

from pibake.utils import (
    get_filename_from_response,
    remove_existing_file,
    get_filesize,
    get_images,
    get_image_file,
    get_image_source_list,
    get_default_image_source
)
from . import disks
from . import settings


class CookConfig:
    def __init__(self):
        pass


cook_config = click.make_pass_decorator(CookConfig, ensure=True)


@click.group()
@click.version_option(settings.__version__)
@click.option('-v', '--verbose', default=0, count=True, help='Level of verbosity of logs')
@click.option('-c', '--cache-path',
              default=settings.CACHE,
              type=click.Path(),
              help='Image cache path, Default: {}'.format(settings.CACHE))
@cook_config
def cli(config, cache_path, verbose):
    """
    Fetch, manage and burn Raspberry PI images.
    """
    config.verbose = verbose
    config.cache_path = cache_path


@cli.command('fetch')
@click.option('-o', '--overwrite/--no-overwrite', default=False, help='Overwrite existing file')
@click.option('-i', '--image',
              type=click.Choice(get_image_source_list()),
              default=get_default_image_source(),
              help='Download NOOBS Full or Lite')
@cook_config
def fetch(config, image, overwrite):
    """
    Fetch images 
    """

    os.makedirs(config.cache_path, exist_ok=True)

    click.echo('Contacting server...')
    response = requests.get(settings.IMAGE_SOURCE_LOOKUP[image], stream=True)

    fname = get_filename_from_response(response, config.verbose)
    file_size = get_filesize(response)
    cache_file_name = os.path.join(config.cache_path, fname)
    remove_existing_file(cache_file_name, overwrite)

    click.echo('Fetching {}'.format(cache_file_name))
    if response.status_code == 200:
        with open(cache_file_name, 'wb') as f:
            with click.progressbar(length=file_size) as bar:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)
                    bar.update(len(chunk))


@cli.command('list')
@cook_config
def list_images(config):
    """ List all images available in local cache """
    for image in get_images(config):
        click.echo(image)


@cli.command('disks')
@cook_config
def list_images(config):
    """ List mounted SD card(s) that are good candidates to be burned """

    sds = disks.get_mounted_candidates()
    if sds:
        click.echo('{} potential disk(s) are available:'.format(len(sds)))
        for disk in sds:
            click.echo('Device {device} mounted on {mountpoint}'.format(**disk._asdict()))
    else:
        click.echo('No mounted SD cards found. Insert a SD card and format it to vfat.')


@cli.command('bake')
@click.argument('image')
@click.argument('mountpoint')
@cook_config
def bake_image(config, image, mountpoint):
    """
    Bake selected image to disk mounted at mountpoint
    """
    valid_images = get_images(config)
    if image not in valid_images:
        click.echo('Please pick a valid image, current choices are: {}'.format(', '.join(valid_images)))
        sys.exit()

    valid_mounts = [disk.mountpoint for disk in disks.get_mounted_candidates()]
    if mountpoint not in valid_mounts:
        click.echo('Please pick a valid mountpoint, one of {}'.format(', '.join(valid_mounts)))
        sys.exit()

    disks.unzip_to_mount(get_image_file(image), mountpoint)
