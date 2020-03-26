# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import glob
import os
import shutil
import subprocess
import sys

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# sys.path.insert(0, os.path.abspath('.'))

# make source
subprocess.call(['python', './make_source.py', '../cpp', '.'])

# -- Project information -----------------------------------------------------

project = 'sandbox'
copyright = '2020, SecureCo, LLC.'
author = 'SecureCo, LLC.'

# Install dev version of sphinxcontrib_golangdomain if needed
if os.path.isdir('/tmp/sphinxcontrib-golangdomain'):
    shutil.rmtree('/tmp/sphinxcontrib-golangdomain')

golangdomain_cmd = 'git clone https://github.com/SecureCoLLC/sphinxcontrib-golangdomain ' + \
    '/tmp/sphinxcontrib-golangdomain ' + \
    '&& cd /tmp/sphinxcontrib-golangdomain ' + \
    '&& python3.7 setup.py build ' + \
    '&& python3.7 setup.py install'

subprocess.call(golangdomain_cmd, shell=True)

# -- General configuration ---------------------------------------------------

sys.path.append("/tmp/sphinxcontrib-golangdomain")

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.imgmath',
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'breathe',
    'autoapi.extension',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.golangdomain',
]

autoapi_type = 'go'

autoapi_dirs = []
for folder in glob.iglob('../go/**', recursive=True):
    if os.path.isdir(folder):
        print('Folders = {}'.format(folder))
        autoapi_dirs.append(folder)

autoapi_generate_api_docs=True
# autoapi_template_dir='_templates/autoapi'

autoapi_options = [
    'members',
    'inherited-members',
    'undoc-members',
    'private-members',
    'special-members',
    'show-inheritance',
    'show-inheritance-diagram',
    'show-module-summary',
]

autoapi_modules = {
   'sandbox': {
        'prune': False,
        'override': True,
        'output': 'auto',
   }
}

autoapi_keep_files=True

breathe_projects = { "sandbox": "doxygen/xml/" }
breathe_default_project = "sandbox"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [ '_index.rst' ]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

class DoxygenRunner:
    def run(self, ):
        """Run the doxygen make command in the designated folder"""

        try:
            retcode = subprocess.call('pwd && cd .. && scripts/doxygen.sh', shell=True)
            if retcode < 0:
                sys.stderr.write("doxygen terminated by signal %s" % (-retcode))
        except OSError as e:
            sys.stderr.write("doxygen execution failed: %s" % e)


    def generate(self, app):
        """Run the doxygen make commands if we're on the ReadTheDocs server"""

        read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'

        if read_the_docs_build:
            self.run()

def setup(app):

    doxygen = DoxygenRunner()

    # Add hook for building doxygen xml when needed
    app.connect("builder-inited", doxygen.generate)
