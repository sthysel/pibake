import os

IMAGE_SOURCE_LOOKUP = {
    'NOOBS': os.getenv('PIBAKE_NOOBS_LATEST_URL', 'https://downloads.raspberrypi.org/NOOBS_latest'),
    'NOOBS_LITE': os.getenv('PIBAKE_NOOBS_LITE_LATEST_URL', 'https://downloads.raspberrypi.org/NOOBS_lite_latest'),
    'RASPIAN': 'https://downloads.raspberrypi.org/raspbian_latest',
    'RASPIAN_LITE': 'https://downloads.raspberrypi.org/raspbian_latest',
}

# where to store the downloaded images
CACHE = os.getenv('PIBAKE_CACHE', os.path.join(os.path.expanduser('~'), '.pibake'))
