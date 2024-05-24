# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Techworks Best Practices in AI'
copyright = '2024'
author = 'Best Practices Working Group'

# The full version, including alpha/beta/rc tags
release = 'v0.5.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['rst2pdf.pdfbuilder']
pdf_documents = [('index', u'best-practices-guide',
                  u'Techworks Best Practices in AI',
                  u'Best Practices Working Group'),]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Fixes some obscure sphinx bug that stops references being tracked
language = 'en'
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
# html_theme_path = ["_themes"]

html_logo = "_static/twheaderlogo.png"



html_theme_options = {
    "announcement": 
    "Get involved with Techworks best practices in AI\
    <a href='https://techworkshub.github.io/best-practice-guide/index.html#getting-involved'>here</a>",
    "sidebar_hide_name": "True",
    "light_css_variables": {
        "color-announcement-background": "#4d8fbacc",
        "font-stack": "Open Sans,sans-serif",
        "color": "#676767",
        "color-foreground-primary" : "#333333",
        "color-brand-primary": "#106098",
        "color-brand-content": "#4d8fba",
        "color-admonition-background": "orange",
    },
}