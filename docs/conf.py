# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.

import os
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

# -- Load Single-Sourced Config --------------- --- --  -

path = Path(__file__, '../../config.py').resolve()
spec = spec_from_file_location("config", path)
config = module_from_spec(spec)
spec.loader.exec_module(config)

# -- Path setup --------------- --- --  -

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

sys.path.insert(0, os.path.abspath('..'))

# -- General configuration --------------- --- --  -
# See http://www.sphinx-doc.org/en/master/config

author = config.author
copyright = config.copyright
description = config.description
name = config.name
project = config.project
release = config.release
repo = config.repo
version = config.version

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '3.3.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.todo',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    # 'sphinx-jsonschema'
    # 'sphinxcontrib.bibtex',
    'pydata_sphinx_theme',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# default_role = 'any'
# suppress_warnings = ['app.add_directive']

# add option to include to do boxes
todo_include_todos = True

# -- Options for sphinx.ext.autodoc --------------- --- --  -

autoclass_content = 'both'
autodoc_default_options = {
    'inherited-members': True,
    'members': True,
    'show-inheritance': True,
    'undoc-members': True,
}
autodoc_member_order = 'bysource'
autodoc_typehints = "description"

# -- Options for HTML output --------------- --- --  -
# See http://www.sphinx-doc.org/en/master/usage/configuration.html#options-
# for-html-help-output

html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "external_links": [],
    # "github_url": "https://github.com/pandas-dev/pandas",
    # "twitter_url": "https://twitter.com/pandas_dev",
    # "google_analytics_id": "UA-27880019-2",
}
html_logo = "_static/logo_small.png"

# html_baseurl = "https://ominatechnologies.github.io/opyprint/"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static", "_static/.nojekyll"]
html_extra_path = [".nojekyll"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
html_sidebars = {
    '**': ['globaltoc.html', 'searchbox.html'],
}

html_copy_source = False
html_show_sourcelink = True
html_show_copyright = True

# The name of math_renderer extension for HTML output. Defaults to 'mathjax'.
html_math_renderer = 'mathjax'

# -- Options for HTMLHelp output --------------- --- --  -

# Output file base name for HTML help builder.
htmlhelp_basename = f'{name}doc'

# -- Options for LaTeX output --------------- --- --  -

latex_preamble = r"""
\usepackage{amsmath,amsfonts,amssymb,amsthm}
\usepackage{graphicx}
\usepackage{fancyhdr}
\usepackage{color}
\usepackage{transparent}
\usepackage{eso-pic}
\usepackage{lipsum}
\usepackage{footnotebackref}

% reduce spacing for itemize:
%\usepackage{enumitem}
%\setlist{nosep}

\setcounter{secnumdepth}{4}
\setcounter{tocdepth}{2}
\pagestyle{fancy}
\makeatletter
  % Update normal pages:
  \fancypagestyle{normal}{
    \fancyhf{}
    \fancyhead[LE,RO]{{\py@HeaderFamily FrozenDict v\version}}
    \fancyfoot[LE,RO]{{\py@HeaderFamily\thepage}}
    \fancyfoot[LO]{{\py@HeaderFamily\nouppercase{\rightmark}}}
    \fancyfoot[RE]{{\py@HeaderFamily\nouppercase{\leftmark}}}
    \renewcommand{\headrulewidth}{0.4pt}
    \renewcommand{\footrulewidth}{0.4pt}
  }
  % Update the first page of each chapter:
  \fancypagestyle{plain}{
    \fancyhf{}
    \fancyfoot[LE,RO]{{\py@HeaderFamily\thepage}}
    \renewcommand{\headrulewidth}{0.4pt}
    \renewcommand{\footrulewidth}{0.4pt}
  }
\makeatother
"""

latex_commands = {
    'tuple': ("{\\langle{#1}\\rangle}", 1),  # e.g. :math:`\tuple{a, b}`
    'foo': "{\\operatorname{foo}}",  # e.g. :math:`\foo_i`
}


def newcommand(name, spec) -> str:
    if isinstance(spec, str):
        pattern = "\\newcommand{{\\{}}}{}"
        return pattern.format(name, spec)
    elif isinstance(spec, tuple):
        pattern = "\\newcommand{{\\{}}}[{}]{}"
        return pattern.format(name, spec[1], spec[0])
    else:
        raise TypeError(f"Unexpected spec for command '{name}': '{spec}'")


def get_preamble() -> str:
    lines = [latex_preamble]
    for command in latex_commands:
        lines.append(newcommand(command, latex_commands[command]))
    return "\n".join(lines)


latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '11pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': get_preamble(),

    # Latex figure (float) alignment
    # 'figure_align': 'htbp',

    'fncychap': '\\usepackage{fncychap}',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [(
    master_doc,
    f'{name}.tex',
    f'{project} Documentation',
    author,
    'manual',
)]

# Set to True if you want all displayed math to be numbered. Defaults to False.
math_number_all = True

# A string that are used for format of label of references to equations. As a
# special character, {number} will be replaced to equation number.
math_eqref_format = 'Eq. {number}'

# If True, displayed math equations are numbered across pages when numfig is
# enabled. The numfig_secnum_depth setting is respected. The eq, not numref,
# role must be used to reference equation numbers. Default is True.
math_numfig = True

# -- Options for sphinx.ext.mathjax --------------- --- --  -

# See https://www.sphinx-doc.org/en/master/usage/extensions/math.html#module-
# sphinx.ext.mathjax
mathjax_config = {
    'TeX': {
        'Macros': latex_commands,
    },
}

# -- Options for sphinx.ext.intersphinx --------------- --- --  -

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# -- Options for manual page output --------------- --- --  -

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(
    master_doc,
    name,
    f'{project} Documentation',
    [author],
    1,
)]

# -- Options for Texinfo output --------------- --- --  -

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [(
    master_doc,
    name,
    f'{project} Documentation',
    author,
    project,
    description,
    'Miscellaneous',
)]
