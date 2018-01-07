# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

"""
Placeholder classes.

Replace this module for the actual code.
"""

__author__ = 'Bernardo MartÃ­nez Garrido'
__license__ = 'MIT'


class AbstractPlaceholder(object):
    """
    Placeholde for an abstract class.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def method(self):
        """
        An abstract method.
        """
        raise NotImplementedError('The roll method must be implemented')


class Placeholder(AbstractPlaceholder):
    """
    An extension of the abstract placeholder.
    """

    def __init__(self, data):
        super(Placeholder, self).__init__()
        self._field = data

    def __str__(self):
        return '%s' % self.field

    def __repr__(self):
        return '<class %s>(field=%r)' % \
               (self.__class__.__name__, self.field)

    @property
    def field(self):
        """
        A field in the placeholder class.

        :return: the field content
        """
        return self._field

    @field.setter
    def field(self, field):
        self._field = field

    def method(self):
        pass
