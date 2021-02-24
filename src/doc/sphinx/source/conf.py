# -*- coding: utf-8 -*-
#
# n2p2 - A neural network potential package documentation build configuration file, created by
# sphinx-quickstart on Tue Jan 29 14:37:49 2019.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'breathe',
#    'exhale',
    'sphinx.ext.mathjax'
]

# Setup the breathe extension
breathe_projects = {
    "n2p2": "../../../../doc/doxygen/xml"
}

breathe_default_project = "n2p2"

## From https://exhale.readthedocs.io/en/latest/usage.html#customizing-breathe-output
#from exhale import utils
#def specificationsForKind(kind):
#    '''
#    For a given input ``kind``, return the list of reStructuredText specifications
#    for the associated Breathe directive.
#    '''
#    # Change the defaults for .. doxygenclass:: and .. doxygenstruct::
#    if kind == "class" or kind == "struct":
#        return [
#          ":members:",
#          ":protected-members:",
#          ":private-members:",
#          ":undoc-members:"
#        ]
#    # Change the defaults for .. doxygenenum::
#    elif kind == "enum":
#        return [":no-link:"]
#    # An empty list signals to Exhale to use the defaults
#    else:
#        return []

## Setup the exhale extension
#exhale_args = {
#    # These arguments are required
#    "containmentFolder":     "./doc-exhale",
#    "rootFileName":          "root.rst",
#    "rootFileTitle":         "n2p2 code documentation",
#    "doxygenStripFromPath":  "..",
#    # Suggested optional arguments
#    "createTreeView":        True,
#    # TIP: if using the sphinx-bootstrap-theme, you need
#    # "treeViewIsBootstrap": True,
#    "exhaleExecutesDoxygen": True,
#    "exhaleDoxygenStdin":    "INPUT = ../../../libnnp\n"
#                             "INPUT += ../../../libnnpif\n" 
#                             "INPUT += ../../../libnnptrain\n" 
#                             "XML_PROGRAMLISTING     = YES\n"
#                             "EXTRACT_ALL            = YES\n"
#                             "EXTRACT_PRIVATE        = YES\n"
#                             "EXTRACT_STATIC         = YES\n"
#                             "EXTRACT_LOCAL_CLASSES  = YES\n",
#    "customSpecificationsMapping": utils.makeCustomSpecificationsMapping(specificationsForKind)
#
#}

## Tell sphinx what the primary language being documented is.
primary_domain = 'cpp'

## Tell sphinx what the pygments highlight language should be.
highlight_language = 'cpp'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'n2p2 - A neural network potential package'
copyright = u'2020, Andreas Singraber'
author = u'Andreas Singraber'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
with open('../../../libnnp/version.h') as f:
    for line in f:
        if 'N2P2_GIT_VERSION' in line:
            version = line.split()[2]
#version = u'1.0.0'
# The full version, including alpha/beta/rc tags.
#release = u'1.0.0'
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}
html_theme_options = {
    'canonical_url': '',
    #'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    #'vcs_pageview_mode': '',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': -1,
    'includehidden': True,
    'titles_only': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'n2p2-Aneuralnetworkpotentialpackagedoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'n2p2-Aneuralnetworkpotentialpackage.tex', u'n2p2 - A neural network potential package Documentation',
     u'Andreas Singraber', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'n2p2-aneuralnetworkpotentialpackage', u'n2p2 - A neural network potential package Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'n2p2-Aneuralnetworkpotentialpackage', u'n2p2 - A neural network potential package Documentation',
     author, 'n2p2-Aneuralnetworkpotentialpackage', 'One line description of project.',
     'Miscellaneous'),
]



