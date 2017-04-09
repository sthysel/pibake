# pibake raspberry pi baker

This tool fetches the latest NOOBS image from source and burns it to a nominated sd-card.

All downloads are kept in local cache directory, `.pibake` by default.
New images have new names so old versions are kept until deleted.


# Usage

To get help

``` bash
Usage: pibake [OPTIONS] COMMAND [ARGS]...

  Fetch, manage and burn Raspberry PI images.

Options:
  -v, --verbose          Level of verbosity of logs
  -c, --cache-path PATH  Image cache path, Default: /home/thys/.pibake
  --help                 Show this message and exit.

Commands:
  fetch  Fetch images
  list   List all images available in local cache

```

Fetch the lates lite NOOBS image

``` bash
$ pibake fetch -o
Contacting server...
Fetching /home/thys/.pibake/NOOBS_lite_v2_3.zip
  [####################################]  100%

```

Fetch the latest full NOOBS image

``` bash
$ pibake fetch --full
Contacting server...
Fetching /home/thys/.pibake/NOOBS_v2_3_0.zip
  [####--------------------------------]   13%  0d 00:17:29
```


To see where the images are retrieved from use the `-vv` option


``` bash
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
```

# Install


## Install from source into virtualen

```
$ workon pibake
$ pip install pibake
```


## Intall from source to local user in .local/

For this to be most usefull have ${HOME}/.local/bin/ in $PATH

``` bash
$ pip install -r requirements.txt
$ pip install --user .
```

