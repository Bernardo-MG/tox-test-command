================
tox Test Command
================

Command for running tox tests with `setuptools`_.

This way the usual command for running tests will call tox:

```
$ python setup.py test
```

To achieve this the project should be using setuptools, and contain a setup.py
file, where the test command will be overriden.

This is detailed in the usage section.

--------
Features
--------

- Running test with tox in any project using setuptools
- Running a specific tox profile

.. toctree::
   :hidden:

   acquire
   usage
   reports
   code/index
