from setuptools import setup, find_packages

setup(
    name='pibake',
    version='0.1',
    description='Manages Rasperri PI Images',
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
