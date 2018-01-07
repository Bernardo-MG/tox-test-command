# -*- coding: utf-8 -*-

import unittest

from bernardomg.tox_test_command import ToxTestCommand

"""
Placeholder tests.
"""

__author__ = '{{ cookiecutter.developer_name }}'
__license__ = 'MIT'


class TestPlaceholder(unittest.TestCase):
    """
    Placeholder for a test case.
    """

    def setUp(self):
        """
        Here the tests environment would be prepared.
        """
        self.command = ToxTestCommand()

    def test_true(self):
        """
        A placeholder test which is always true.
        """
        self.assertTrue(True)
