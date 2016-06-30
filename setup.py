# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages


README_FILE = os.path.join(os.path.dirname(__file__), 'README.rst')

setup(
    name='tomako',
    version='0.1.0.post1',
    description='Tomako is the easiest way to use Mako as a template engine '
                'for Tornado',
    long_description=open(README_FILE).read(),
    keywords=['tomako', 'mako', 'tornado'],
    author='Rodrigo Machado',
    author_email='rcmachado@gmail.com',
    url='https://github.com/rcmachado/tomako',
    license='MIT',
    packages=find_packages(),
    package_dir={'tomako': 'tomako'},
    install_requires=[
        "tornado>=2.3",
        "Mako>=0.7.2",
    ],
    include_package_data=True
)
