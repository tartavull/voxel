#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='voxel',
    version='0.1.0',
    description="voxel",
    long_description=readme + '\n\n' + history,
    author="Ignacio Tartavull",
    author_email='tartavull@gmail.com',
    url='https://github.com/tartavull/voxel',
    packages=[
        'voxel',
    ],
    package_dir={'voxel':
                 'voxel'},
    entry_points={
        'console_scripts': [
            'voxel=voxel.cli:main'
        ]
    },
    include_package_data=True,
    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.xml', '*.html', '*.js']
    },
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='voxel',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
