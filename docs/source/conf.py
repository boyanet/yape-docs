# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'YAPE区块链隐私计算框架'
copyright = '2022, YAPE'
author = 'YAPE'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = "blockchain.png"
html_theme_options = {
    'logo_only': False,
    'display_version': False,
}


# -- Options for EPUB output
epub_show_urls = 'footnote'
