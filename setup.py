# coding: utf-8

from setuptools import setup, find_packages


# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools


setup(
    name="test_api",
    version="0.0.1",
    description="Test API",
    long_description="",
    author_email="invartam@gmail.com",
    url="benjy.lu",
    install_requires=[
        "connexion"
    ],
    packages=find_packages(),
    package_data={'': ['spec/api.yaml']},
    include_package_data=True,
)
