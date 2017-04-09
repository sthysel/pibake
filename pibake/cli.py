import os
import sys
from pprint import pformat

import click
import requests

from . import settings


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


class CookConfig:
    def __init__(self):
        pass


cook_config = click.make_pass_decorator(CookConfig, ensure=True)


@click.group()
@click.option('-v', '--verbose', default=0, count=True, help='Level of verbosity of logs')
@cook_config
def cli(config, verbose):
    """
    Fetch, manage and burn Raspberry PI images.
    """
    config.verbose = verbose


@cli.command('fetch')
@click.option('-o', '--overwrite/--no-overwrite', default=False, help='Overwrite existing file')
@click.option('-c', '--cache-path',
              default=settings.CACHE,
              type=click.Path(),
              help='Image cache path, Default: {}'.format(settings.CACHE))
@click.option('-f', '--full/--lite', default=False, help='Download NOOBS Full or Lite')
@cook_config
def fetch(config, full, cache_path, overwrite):
    """
    Fetch images 
    """
    os.makedirs(cache_path, exist_ok=True)

    if full:
        url = settings.NOOBS_LATEST_URL
    else:
        url = settings.NOOBS_LITE_LATEST_URL

    click.echo('Contacting server...')
    response = requests.get(url, stream=True)

    fname = get_filename_from_response(response, config.verbose)
    file_size = get_filesize(response)
    cache_file_name = os.path.join(cache_path, fname)
    remove_existing_file(cache_file_name, overwrite)

    click.echo('Fetching {}'.format(cache_file_name))
    if response.status_code == 200:
        with open(cache_file_name, 'wb') as f:
            with click.progressbar(length=file_size) as bar:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)
                    bar.update(len(chunk))
