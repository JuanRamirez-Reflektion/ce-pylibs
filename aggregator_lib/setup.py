import os

from setuptools import setup, find_packages

__version = '1.0.2'

requires = [
    'pyramid>=1.4',
    'coveralls',
]

packages = [
    'product_aggregator'
]

setup(
    name='product_aggregator',
    version=__version,
    description='aggregation library for products',
    classifiers=[
        'Programming Language :: Python'
    ],
    author='Juan Ramirez',
    author_email='juanpaulomdq@gmail.com',
    keywords=['sarasa'],
    url='',
    include_package_data=False,     # do not want version control data
    packages=find_packages(),
    zip_safe=False,
    install_requires=requires,
    entry_points={}
)
