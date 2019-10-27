import os
import sys
from pathlib import Path
from pprint import pformat
from typing import List

import click

from . import settings

image_lookup = {}


def get_image_source_list():
    return sorted(settings.IMAGE_SOURCE_LOOKUP.keys())


def get_default_image_source():
    return get_image_source_list()[0]


def get_filename_from_response(response, verbose=0):
    """
    :param response: The response object from requests
    :param verbose: Chattiness
    :return:
    """
    if verbose >= 2:
        click.echo(pformat(dict(**response.headers)))
        for r in response.history:
            click.echo(pformat(dict(**r.headers)))

    try:
        location = response.history[0].headers.get('Location')
        filename = location.split('/')[-1]
    except:
        raise ValueError('Could not find a filename')
    else:
        return filename


def remove_existing_file(cache_file_name, overwrite):
    if os.path.isfile(cache_file_name):
        if overwrite:
            os.remove(cache_file_name)
        else:
            click.secho(
                f'{cache_file_name} already exists. Use the --override option to re-download',
                fg='red')
            sys.exit()


def get_filesize(response):
    try:
        return int(response.headers.get('Content-Length'))
    except ValueError:
        return -1


def get_images(config) -> List:
    """
    List of images available in cache
    :param config:
    :return:
    """

    image_folder = Path(config.cache_path)
    if image_folder.exists():
        for z in image_folder.glob('*.zip'):
            image_lookup[z.name] = z
        return sorted(image_lookup.keys())
    else:
        return []


def get_image_file(name):
    return image_lookup.get(name, None)
