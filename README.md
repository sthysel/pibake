# pibake raspberry pi baker

This tool fetches the latest NOOBS image from source and burns it to a nominated sd-card.

All downloads are kept in local cache directory, `.pibake` by default.
New images have new names so old versions are kept until deleted.


# Usage

To get help

```
pibake --help
Usage: pibake [OPTIONS] COMMAND [ARGS]...

  Fetch, manage and burn Raspberry PI images.

Options:
  -v, --verbose  Level of verbosity of logs
  --help         Show this message and exit.

Commands:
  fetch  Fetch images
```

Fetch the lates lite NOOBS image

```
$ pibake fetch -o
Contacting server...
Fetching /home/thys/.pibake/NOOBS_lite_v2_3.zip
  [####################################]  100%

```

Fetch the latest full NOOBS image

```
$ pibake fetch --full
Contacting server...
Fetching /home/thys/.pibake/NOOBS_v2_3_0.zip
  [####--------------------------------]   13%  0d 00:17:29
```
