#!/usr/bin/env python

import os
import sys
from setuptools import setup

base_dir = os.path.dirname(__file__)
src_dir = os.path.join(base_dir, "src")

# When executing the setup.py, we need to be able to import ourselves, this
# means that we need to add the src/ directory to the sys.path.
sys.path.insert(0, src_dir)

requirements = [
    'cryptography (>=2.8.0, <3.0.0)',
    'future (>=0.18.2)',
    'pytz (>=2019.3)'
]

setup(name='adyen-cse-python',
      version='0.2.0',
      description='[UNOFFICIAL] Adyen Client-side encryption library for Python',
      author='Michael Cheah',
      author_email='michael@cheah.xyz',
      url='https://github.com/cheah/adyen-cse-python',
      packages=['adyen_cse_python'],
      package_dir={'': 'src'},
      install_requires=requirements
      )
