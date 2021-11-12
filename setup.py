from distutils.core import setup
from setuptools import find_packages
setup(name='ru01rejo',
version='0.1',
author='DSSS',
author_email='patricia.urban@fau.de',
packages=find_packages(),
install_requires=['numpy', 'Pillow', 'ipywidgets'])