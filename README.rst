===============================
tox Test Command
===============================

Command for running tox tests with `setuptools`_.

This way the usual command for running tests will call tox:

```
$ python setup.py test
```

To achieve this the project should be using setuptools, and contain a setup.py
file, where the test command will be overriden.

This is detailed in the usage section.

.. image:: https://badge.fury.io/py/bernardomg.tox-test-command.svg
    :target: https://pypi.python.org/pypi/bernardomg.tox-test-command
    :alt: tox Test Command Pypi package page

.. image:: https://img.shields.io/badge/docs-release-blue.svg
    :target: http://docs.bernardomg.com/tox-test-command
    :alt: tox Test Command latest documentation Status
.. image:: https://img.shields.io/badge/docs-develop-blue.svg
    :target: http://docs.bernardomg.com/development/tox-test-command
    :alt: tox Test Command development documentation Status

Features
--------

- Running test with tox in any project using setuptools
- Running a specific tox profile

Documentation
-------------

Documentation sources are included with the project, and used to generate the
documentation sites:

- The `latest docs`_ are always generated for the latest release, kept in the 'master' branch
- The `development docs`_ are generated from the latest code in the 'develop' branch

You can also create the documentation from the source files, kept in the 'docs'
folder, with the help of `Sphinx`_. For this use the makefile, or the make.bat
file, contained on that folder.

Prerequisites
~~~~~~~~~~~~~

The project has been tested in the following versions of the interpreter:

- Python 2.7
- Python 3.4
- Python 3.5
- Python 3.6
- Pypy
- Pypy 3

All other dependencies are indicated on the requirements.txt file.

These can be installed with:

``$ pip install --upgrade -r requirements.txt``

Installing
~~~~~~~~~~

The project is offered as a `Pypi package`_, and using pip is the preferred way
to install it. For this use the following command;

``$ pip install tox-test-command``

If needed, manual installation is possible:

``$ python setup.py install``

Usage
-----

The application has been coded in Python, and is meant for projects using `setuptools`_.

It can be used to override the default test command with ease::

    from bernardomg.tox_test_command import ToxTestCommand

    setup(
        ...
        cmdclass={'test': ToxTestCommand},
        ...
    )

This way the usual command for running tests will call the new command:

```
$ python setup.py test
```

It is possible to run a specific tox profile:

```
$ python setup.py test -p [profile-name]
```

Testing
-------

The tests included with the project can be run with:

``$ python setup.py test``

This will delegate the execution to tox.

It is possible to run just one of the test profiles, in this case the py36 profile:

``$ python setup.py test -p "py36"``

Collaborate
-----------

Any kind of help with the project will be well received, and there are two main ways to give such help:

- Reporting errors and asking for extensions through the issues management
- or forking the repository and extending the project

Issues management
~~~~~~~~~~~~~~~~~

Issues are managed at the GitHub `project issues tracker`_, where any Github
user may report bugs or ask for new features.

Getting the code
~~~~~~~~~~~~~~~~

If you wish to fork or modify the code, visit the `GitHub project page`_, where
the latest versions are always kept. Check the 'master' branch for the latest
release, and the 'develop' for the current, and stable, development version.

License
-------

The project has been released under the `MIT License`_.

.. _GitHub project page: https://github.com/Bernardo-MG/tox-test-command
.. _latest docs: http://docs.bernardomg.com/tox-test-command
.. _development docs: http://docs.bernardomg.com/development/tox-test-command
.. _Pypi package: https://pypi.python.org/pypi/bernardomg.tox-test-command
.. _MIT License: http://www.opensource.org/licenses/mit-license.php
.. _project issues tracker: https://github.com/Bernardo-MG/tox-test-command/issues
.. _Sphinx: http://sphinx-doc.org/

.. _setuptools: https://github.com/pypa/setuptools
