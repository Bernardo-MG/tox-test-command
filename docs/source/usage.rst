=====
Usage
=====

The application is meant for projects using `setuptools`_.

It can be used to override the default test command with ease::

    import tox-test-command as test_command

    setup(
        ...
        cmdclass={'test': test_command},
        ...
    )

-------
Testing
-------

The tests included with the project can be run with:

.. code::

    $ python setup.py test

This will delegate the execution to tox.

It is possible to run just one of the test profiles, in this case the py36 profile:

.. code::

    $ python setup.py test -p "py36"

.. _setuptools: https://github.com/pypa/setuptools
