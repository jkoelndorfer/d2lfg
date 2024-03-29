from pathlib import Path
import sys

from d2lfg import __version__

sphinx_conf_dir = Path(__file__).cwd()
repo_root = (sphinx_conf_dir / ".." / "..").resolve()
src_dir = repo_root / "src"

# Allow sphinx to discover the "tests" module.
sys.path.insert(0, str(repo_root))

# Allow sphinx to discover d2lfg.
sys.path.insert(0, str(src_dir))


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "d2lfg"
copyright = "2024, John Koelndorfer"
author = "John Koelndorfer"
release = __version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
]

templates_path = ["_templates"]
exclude_patterns = []

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# Prevent Sphinx from including the entire module name in
# class autodocs.
add_module_names = False

# Disables Sphinx nitpicking (i.e. ability to link to docs) for
# specific targets.
#
# See https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-nitpick_ignore_regex
nitpick_ignore_regex = [
    # Sphinx does not know how to resolve TypeVars.
    #
    # See https://github.com/sphinx-doc/sphinx/issues/10974.
    (r"py:class", r".*\.T"),
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
