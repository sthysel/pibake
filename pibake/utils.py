import os
import sys
from pprint import pformat

import click
from . import settings


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
            click.secho('{} already exists. Use the --override option to re-download'.format(cache_file_name), fg='red')
            sys.exit()


def get_filesize(response):
    try:
        return int(response.headers.get('Content-Length'))
    except ValueError:
        return -1


image_lookup = {}


def get_images(config):
    """
    List of images available in cache
    :param config: 
    :return: 
    """
    for file in os.listdir(config.cache_path):
        if file.endswith('.zip'):
            image_lookup[file.split('.')[0]] = os.path.join(config.cache_path, file)
    return sorted(image_lookup.keys())


def get_image_file(name):
    return image_lookup.get(name, None)
