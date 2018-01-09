#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# tox Test Command documentation build configuration file.

import ast
import re
import sys
import os
import datetime
from codecs import open
from os import path

# -- Version --------------------------------------------------------------

# Regular expression for the version
_version_re = re.compile(r'__version__\s+=\s+(.*)')

# Path to the project's root
here = path.abspath(path.dirname(__file__))

# Gets the version for the source folder __init__.py file
with open('../../tox_test_command/__init__.py', 'rb',
          encoding='utf-8') as f:
    version_lib = f.read()
    version_lib = _version_re.search(version_lib).group(1)
    version_lib = str(ast.literal_eval(version_lib.rstrip()))

# -- Code location --------------------------------------------------------

sys.path.append(os.path.abspath('../..'))
sys.path.append(os.path.abspath('../../tox-test-command'))


# -- General configuration ------------------------------------------------

# Sphinx extensions
#
# autodoc: generates documentation from docstrings
# intersphinx: generates links to other Sphinx-created docs
# viewcode: generates HTML from code sources
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

# Templates.
templates_path = ['_templates']

# Only reStructuredText is accepted
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# Sort members by type
autodoc_member_order = 'groupwise'

# General information about the project.
project = 'tox Test Command'
project_safe = project.replace(' ', '_')
copyright = u'2018, Bernardo MartÃ­nez Garrido'
authors = [u'Bernardo MartÃ­nez Garrido']

# The version info for the project.
#
# Semantic version value.
version = version_lib
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

import sphinx_docs_theme

# Activate the theme.
html_theme = 'sphinx_docs_theme'
html_theme_path = sphinx_docs_theme.get_html_theme_path()

# Removes permalink markers
html_add_permalinks = ''

# Theme options.
html_theme_options = {
    'keywords': '',
    'author_name': ','.join(authors),
    'author_url': 'https://github.com/Bernardo-MG',
    'twitter_id': '@Bernardo-MG',
    'publish_date': datetime.datetime.now().date(),
    'years': datetime.datetime.now().year,
    'scm_name': 'Github',
    'scm_url': 'https://github.com/Bernardo-MG/tox-test-command',
    'ci_name': 'Travis',
    'ci_url': 'https://travis-ci.org/Bernardo-MG/tox-test-command',
    'issues_name': 'Github',
    'issues_url': 'https://github.com/Bernardo-MG/tox-test-command/issues',
    'releases_repos': [
        ('Pypi',
         'https://pypi.python.org/pypi/bernardomg.tox-test-command')],
    'general_info_links': [('Acquire', './acquire.html'),
                           ('Usage', './usage.html')],
    'navbar_links': [('Documentation', [('Acquire', './acquire.html'),
                                        ('Usage', './usage.html')]),
                     ('Info and Reports', [('Reports', './reports.html'),
                                           ('Code docs', './code/index.html')])],
}

# Output file base name for HTML help builder.
htmlhelp_basename = '%s doc' % project

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
}

# List of LaTeX documents.
latex_documents = [
    (master_doc, '%s.tex' % project_safe, '%s Documentation' % project,
     ','.join(authors), 'manual'),
]


# -- Options for manual page output ---------------------------------------

# List of manual pages.
man_pages = [
    (master_doc, project, '%s Documentation' % project,
     [','.join(authors)], 1)
]


# -- Options for Texinfo output -------------------------------------------

# List of Texinfo documents.
texinfo_documents = [
    (master_doc, project, '%s Documentation' % project,
     ','.join(authors), project, 'setuptools command for running tests using tox',
     'Miscellaneous'),
]


# -- Intersphinx links ----------------------------------------------------

# Intersphinx mapping.
intersphinx_mapping = {
    'https://docs.python.org/': None,
}
