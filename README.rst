Raspberry pi image baker
========================

.. image:: https://readthedocs.org/projects/pibake/badge/?version=latest
   :target: http://pibake.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

This tool fetches the latest Raspberry PI images from the official
sources and keeps it in a local cache. You can then burn the image to SD
card from the cached copy.

Using the tool allows you to script PI installs using the latest images
and prevents unfortunate mishaps when writing it to the SD card.

All downloads are kept in local XDG specified cache directory,
``~/.cache/pibake`` by default.

New images have new names so old versions are kept until manually
deleted from the cache.

This means the images are always at hand and you can update your local
copies when and if required.

Usage
=====

To get help

.. code:: bash

    $ pibake --help
    Usage: pibake [OPTIONS] COMMAND [ARGS]...

      Fetch, manage and burn Raspberry PI images.

    Options:
      -v, --verbose          Level of verbosity of logs
      -c, --cache-path PATH  Image cache path, Default: /home/thys/.cache/pibake
      --help                 Show this message and exit.

    Commands:
      bake   Bake selected image to disk mounted at...
      disks  List mounted SD card(s) that are good...
      fetch  Fetch images
      list   List all images available in local cache

Fetching images

::

    $ pibake fetch --help
    Usage: pibake fetch [OPTIONS]

      Fetch images

    Options:
      -o, --overwrite / --no-overwrite
                                      Overwrite existing file
      -i, --image [NOOBS|NOOBS_LITE|RASPIAN|RASPIAN_LITE]
                                      Download NOOBS Full or Lite
      --help                          Show this message and exit.

Fetch the latest lite NOOBS image

.. code:: bash

    $ pibake fetch NOOBS
    Contacting server...
    Fetching /home/thys/.pibake/NOOBS_lite_v2_3.zip
      [####################################]  100%

Fetch the latest full NOOBS image

.. code:: bash

    $ pibake fetch --full
    Contacting server...
    Fetching /home/thys/.pibake/NOOBS_v2_3_0.zip
      [####--------------------------------]   13%  0d 00:17:29

View potential SD cards to bake a image on. Most distributions will
automount a disk when inserted. Applications like nautilus will also
mount all available disks.

::

    $ pibake disks
    1 potential disk(s) are available:
    Device /dev/sdb1 mounted on /run/media/thys/A881-FFA5

To list all images available locally

::

    $ pibake list
    2017-03-02-raspbian-jessie
    NOOBS_lite_v2_3
    NOOBS_v2_3_0
    NOOBS_v2_4_0

To see where the images are retrieved from use the ``-vv`` option

.. code:: bash

    pibake -vv fetch
    Contacting server...
    {'Accept-Ranges': 'bytes',
     'Age': '2714',
     'Content-Length': '33492713',
     'Content-Type': 'application/zip',
     'Date': 'Sun, 09 Apr 2017 09:31:57 GMT',
     'ETag': '"140006-1ff0ee9-549d637969e00"',
     'Last-Modified': 'Fri, 03 Mar 2017 16:41:28 GMT',
     'Server': 'Apache/2.2.22 (Debian)',
     'Via': '1.1 d.cdn.velocix.com:80 (pcd/42.0.189164.189164 (2016-03-03 08:58:06 '
            'UTC))',
     'X-Cache': 'HIT from d.cdn.velocix.com'}
    {'Connection': 'close',
     'Content-Encoding': 'gzip',
     'Content-Length': '278',
     'Content-Type': 'text/html; charset=iso-8859-1',
     'Date': 'Sun, 09 Apr 2017 10:17:08 GMT',
     'Location': 'https://downloads.raspberrypi.org/NOOBS_lite/images/NOOBS_lite-2017-03-03/NOOBS_lite_v2_3.zip',
     'Server': 'Apache/2.2.22 (Debian)',
     'Vary': 'Accept-Encoding'}
    {'Connection': 'close',
     'Content-Encoding': 'gzip',
     'Content-Length': '284',
     'Content-Type': 'text/html; charset=iso-8859-1',
     'Date': 'Sun, 09 Apr 2017 10:17:09 GMT',
     'Location': 'http://director.downloads.raspberrypi.org/NOOBS_lite/images/NOOBS_lite-2017-03-03/NOOBS_lite_v2_3.zip',
     'Server': 'Apache/2.2.22 (Debian)',
     'Vary': 'Accept-Encoding'}
    {'Connection': 'close',
     'Content-Length': '0',
     'Content-Type': 'text/x-python',
     'Date': 'Sun, 09 Apr 2017 10:17:10 GMT',
     'Location': 'http://vx2-downloads.raspberrypi.org/NOOBS_lite/images/NOOBS_lite-2017-03-03/NOOBS_lite_v2_3.zip',
     'Server': 'Apache/2.2.22 (Debian)'}

Install
=======

pibake is in pypi

::

    $ pip install pibake

Install from source into virtualenv
-----------------------------------

::

    $ workon pibake
    $ pip install pibake

Install from source to local user in .local/
--------------------------------------------

For this to be most useful have ${HOME}/.local/bin/ in $PATH

.. code:: bash

    $ pip install -r requirements.txt
    $ pip install --user .

Dev
===

::

    $ bumpversion --current-version=0.2.2 patch
    $ python setup.py sdist bdist_wheel
    $ twine upload -r test -s dist/*
    $ twine upload dist/*
