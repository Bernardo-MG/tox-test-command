# -*- coding: utf-8 -*-

import sys

from setuptools.command.test import test as test_command


class ToxTestCommand(test_command):
    """
    Tox test command.

    Calls tox for running the tests.
    """
    user_options = [
        ('test-module=', 'm', "Run 'test_suite' in specified module"),
        ('test-suite=', 's',
         "Run single test, case or suite (e.g. 'module.test_suite')"),
        ('test-runner=', 'r', "Test runner to use"),
        ('profile=', 'p', 'Test profile to use')
    ]

    def initialize_options(self):
        test_command.initialize_options(self)
        self.profile = None

    def finalize_options(self):
        test_command.finalize_options(self)
        self.test_args = []

        if self.profile is not None:
            # Adds the profile argument
            # For example: '-e=py36'
            self.test_args.append('-e=' + self.profile)

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox

        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)
