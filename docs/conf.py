# -*- coding: utf-8 -*-
"""Sphinx configuration."""
import os
import sys

import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath("../"))

project = "boolean_jaccard"
author = "Ryan B Patterson-Cross"
copyright = "2021-2022, IMS-MRL Bioinformatics and Biostatistic Core"
version = "0.1.1"
extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "myst_parser",
]

napoleon_google_docstrings = False
napoleon_numpy_docstrings = True
napoleon_use_param = False

html_theme = "sphinx_rtd_theme"

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
myst_heading_anchors = 2
