# this is to maintain relative path. by using command : "pip install -e . ", it is helping to add all packages 
# in memory with editable mode. so new files will also be part of the memory automatically.
from setuptools import find_packages, setup


setup(name='APITEST', version='1.0', packages=find_packages())
