# -*- coding: utf-8 -*-
# Copyright (c) 2019 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import os
from setuptools import setup, find_packages


setup(
    name = "MacsecEnableAgent",
    version = "0.1.0",
    author = "Jesse Mather",
    author_email = "jmather@arista.com",
    description = "Macsec enabler agent",
    long_description = "",
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Network Engineers",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Environment :: Functional Testing Automation"
    ],
    url = "http://aristanetworks.com",
    license = "Proprietary",
    options = {
        "bdist_rpm": {
            "post_install" : "scripts/post_install.sh",
            "post_uninstall" : "scripts/post_uninstall.sh"
        }
    },
    #py_modules=['_MacsecEnableAgent'],
    scripts = ['MacsecEnableAgent']
)