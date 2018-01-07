# -*- coding: utf-8 -*-
import io
from os.path import dirname
from os.path import join

from setuptools import find_packages, setup
from bernardomg.tox_test_command import ToxTestCommand
from version_extractor import extract_version_init

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


setup(
    name='bernardomg.tox-test-command',
    packages=find_packages(),
    include_package_data=True,
    package_data={
    },
    version=extract_version_init(_source_package),
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
