#!/usr/bin/env python3

import re
import pathlib
import setuptools

rootdir = pathlib.Path(__file__).parent.resolve()

versionfile = rootdir.joinpath('cimr', '__init__.py')

try:
    with open(versionfile, 'r') as vf:
        vers = vf.read()
        pattern = re.compile(r"^__version__ = ['\"]([^'\"]*)['\"]", re.MULTILINE)
        version = pattern.search(vers).group(1)
except FileNotFoundError:
    version = '0.1.0'
    print('no version file present. check your build version.')

readmefile = rootdir.joinpath('README.md')
with open(readmefile, 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    # module detail
    name='cimr',
    version=version,
    url='https://github.com/greenelab/cimr',
    description='continuous integration of association summary statistics for twas',
    long_description_content_type='text/markdown',
    long_description=long_description,
    license='BSD 3-Clause',

    # author
    author='YoSon Park',

    # topics
    keywords='mr ci twas netwas',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
    ],

    packages=setuptools.find_packages(),

    # Specify python version
    python_requires='>=3.6',

    # Run-time dependencies
    install_requires=[
        'scikit-learn',
        'numpy',
        'pandas',
        'pathlib',
    ],

    # Additional groups of dependencies
    extras_require={
    },

    # Create command line script
    entry_points={
        'console_scripts': [
            'cimr = cimr.prompt:main',
        ],
    },

    # Include package data files from MANIFEST.in
    include_package_data=True,
)
