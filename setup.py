# -*- coding: utf-8 -*-
import io
from os.path import dirname
from os.path import join

from setuptools import find_packages, setup
from tox_test_command import ToxTestCommand

import ast
import re

"""
PyPI configuration module.

This is prepared for easing the generation of deployment files.
"""

__license__ = 'MIT'

# Source package
_source_package = 'tox_test_command/'

# Test requirements
_tests_require = ['tox']


# Gets the long description from the readme
def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


def extract_version(path):
    """
    Reads the file at the specified path and returns the version contained in it.

    This is meant for reading the __init__.py file inside a package, and so it
    expects a version field like:

    __version__ = '1.0.0'

    :param path: path to the Python file
    :return: the version inside the file
    """

    # Regular expression for the version
    _version_re = re.compile(r'__version__\s+=\s+(.*)')

    with open(path + '__init__.py', 'r', encoding='utf-8') as f:
        version = f.read()

    if version:
        version = _version_re.search(version)
        if version:
            version = version.group(1)
            version = str(ast.literal_eval(version.rstrip()))
            extracted = version
        else:
            extracted = None
    else:
        extracted = None

    return extracted


setup(
    name='bernardomg.tox-test-command',
    packages=find_packages(),
    include_package_data=True,
    package_data={
    },
    version=extract_version(_source_package),
    description='setuptools command for running tests using tox',
    author='Bernardo MartÃ\xadnez Garrido',
    author_email='programming@bernardomg.com',
    license='MIT',
    url='https://github.com/Bernardo-MG/tox-test-command',
    download_url='https://pypi.python.org/pypi/bernardomg.tox-test-command',
    keywords=[],
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    long_description=read('README.rst'),
    install_requires=[
        'setuptools',
        'tox'
    ],
    tests_require=_tests_require,
    extras_require={'test': _tests_require},
    cmdclass={'test': ToxTestCommand},
)
