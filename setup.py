#!/usr/bin/env python

from setuptools import setup
# from setuptools.command.build_ext import build_ext
from glob import glob
from setuptools import Extension

import numpy

setup(name='healpylite',
      version="0.1",
      description='Healpix binning for Python',
      packages=['healpylite'],
      ext_modules=[
          Extension('healpylite._healpy_pixel_lib',
            sources=['healpylite/src/_healpy_pixel_lib.cc'] + glob('healpylite/src/planck/*.cc'),
            include_dirs=[numpy.get_include()],
            language='c++'
          ),
      ],
      install_requires=['numpy'],
      setup_requires=['pytest-runner'],
      test_requires=['pytest'],
      license='GPLv2',
      )
