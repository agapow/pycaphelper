from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pycaphelper',
      version=version,
      description="Utilities for working with PyCap (which is itself or working with REDCap)",
      long_description="""\
PyCap wraps the REST API of the REDCap web database system. This package provides a few extra features, including aseveral scripts for  uploading and backing up the database.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='redcap database pycap rest',
      author='Paul Agapow',
      author_email='pual@agapow.net',
      url='http://www.agapow.net/software/pycaphelper',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
