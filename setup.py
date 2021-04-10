#!/usr/bin/env python

# Copyright 2014 Koert van der Veer
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os

from setuptools import setup, find_packages

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REQUIREMENTS_FILE = os.path.join(BASE_DIR, "requirements.txt")

from dist_utils import fetch_requirements

install_reqs, dep_links = fetch_requirements(REQUIREMENTS_FILE)


setup(
    name="logshipper",
    author="Koert van der Veer",
    author_email="koert@ondergetekende.nl",
    summary="Gathers, filters, mangles and redistribute log messages",
    description_file="README.md",
    license="Apache-2",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    install_requires=install_reqs,
    dependency_links=dep_links,
    packages=find_packages(exclude=["setuptools", "tests"]),
    entry_points={
        "console_scripts": [
            "logshipper = logshipper.cmd:main",
            "logshipper-ship-file = logshipper.cmd:ship_file",
        ],
        "logshipper.inputs": [
            "syslog = logshipper.input:Syslog",
            "stdin = logshipper.input:Stdin",
            "tail = logshipper.tail:Tail",
            "command = logshipper.input:Command",
        ],
        "logshipper.filters": [
            "drop = logshipper.filters:prepare_drop",
            "edge = logshipper.filters:prepare_edge",
            "extract = logshipper.filters:prepare_extract",
            "match = logshipper.filters:prepare_match",
            "python = logshipper.filters:prepare_python",
            "replace = logshipper.filters:prepare_replace",
            "set = logshipper.filters:prepare_set",
            "strptime = logshipper.filters:prepare_strptime",
            "unset = logshipper.filters:prepare_unset",
            "timewindow = logshipper.filters:prepare_timewindow",
        ],
        "logshipper.outputs": [
            "call = logshipper.outputs:prepare_call",
            "debug = logshipper.outputs:prepare_debug",
            "elasticsearch = logshipper.elasticsearch:prepare_elasticsearch_http",
            "fork = logshipper.outputs:prepare_fork",
            "jump = logshipper.outputs:prepare_jump",
            "logging = logshipper.pylogging:prepare_logging",
            "rabbitmq = logshipper.outputs:prepare_rabbitmq",
            "statsd = logshipper.outputs:prepare_statsd",
            "stdout = logshipper.outputs:prepare_stdout",
        ]
    },
)
