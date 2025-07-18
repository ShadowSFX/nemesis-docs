# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sistema de Facturación Nemesis'
copyright = '2025, SysNemesis'
author = 'Mauricio Ramírez'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# Prefix document path to section labels, to use:
# `path/to/file:heading` instead of just `heading`
autosectionlabel_prefix_document = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Custom CSS for Godot-style theme
html_css_files = [
    'css/custom.css',
]

# Theme options - updated for current sphinx_rtd_theme
html_theme_options = {
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'style_nav_header_background': '#333f67',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Additional context
html_context = {
    'display_github': False,
}

# HTML title
html_title = "Documentación del Sistema Nemesis"

# Favicon
# html_favicon = '_static/favicon.ico'

# Logo
# html_logo = '_static/logo.png'

# Show "Edit on GitHub" links
html_show_sourcelink = False

# Don't show "Created using Sphinx" in the HTML footer
html_show_sphinx = False
