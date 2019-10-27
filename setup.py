from setuptools import find_packages, setup

long_description = '''
pibake fetches and stores Raspberry PI Images to local cache, from
where you can burn it to a mounted SD card.
'''

setup(author='Thys Meintjes',
      author_email='sthysel@gmail.com',
      name='pibake',
      version='0.2.7',
      keywords='Raspberry PI Downloader',
      long_description=open('README.rst').read(),
      url='https://github.com/sthysel/pibake',
      download_url='https://github.com/sthysel/pibake/archive/v0.2.7.tar.gz',
      license="GPLv2",
      description='Fetches and Manages Raspberry PI Images',
      packages=find_packages(exclude=['tests*']),
      include_package_data=True,
      install_requires=[
          'click',
          'requests',
          'psutil',
          'pyxdg',
          'xdg',
      ],
      entry_points={'console_scripts': [
          'pibake=pibake.cli:cli',
      ]},
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 3.6',
          'Intended Audience :: Education',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Science/Research', 'Operating System :: Unix',
          'Topic :: Education', 'Topic :: Utilities'
      ])
