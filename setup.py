#!/usr/bin/env python
from setuptools import setup
from dydra import __version__

setup(
  name             = 'dydra',
  version          = __version__,
  description      = 'Dydra.com software development kit (SDK) for Python.',
  long_description = open('README').read(),
  author           = 'Dydra.com',
  author_email     = 'dydra@googlegroups.com', # @see http://groups.google.com/group/dydra
  url              = 'http://docs.dydra.com/sdk/python',
  download_url     = 'http://pypi.python.org/pypi/dydra',
  packages         = ['dydra'],
  classifiers      = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: Public Domain',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Database',
    'Topic :: Internet',
    'Topic :: Software Development :: Libraries',
  ],
  license          = 'Public Domain',
  install_requires = ['rdflib>=3.0.0'],
)
