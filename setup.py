from setuptools import setup, find_packages

long_description = '''
Fetches and stores Raspberry PI Images to local cache.
'''

setup(
    author='Thys Meintjes',
    author_email='sthysel@gmail.com',
    name='pibake',
    version='0.1',
    keywords='Raspberry PI Downloader',
    long_description=long_description,
    url='https://github.com/sthysel/pibake',
    license="GPLv2",
    description='Fetches and Manages Raspberry PI Images',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'pibake=pibake.cli:cli',
        ]
    }
)
