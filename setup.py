# -*- coding: utf-8 -*-
import ast
import re
import io
from os.path import dirname
from os.path import join
from codecs import open

from setuptools import find_packages, setup
from bernardomg.tox_test_command import ToxTestCommand

"""
PyPI configuration module.

This is prepared for easing the generation of deployment files.
"""

__license__ = 'MIT'

# Source package
_source_package = 'bernardomg/tox_test_command/'

# Regular expression for the version
_version_re = re.compile(r'__version__\s+=\s+(.*)')

# Test requirements
_tests_require = ['tox']


# Gets the long description from the readme
def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


# Gets the version for the source folder __init__.py file
with open(_source_package + '__init__.py', 'rb',
          encoding='utf-8') as f:
    version_lib = f.read()
    version_lib = _version_re.search(version_lib).group(1)
    version_lib = str(ast.literal_eval(version_lib.rstrip()))


setup(
    name='bernardomg.tox-test-command',
    packages=find_packages(),
    include_package_data=True,
    package_data={
    },
    version=version_lib,
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
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
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
