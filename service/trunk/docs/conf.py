# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))

extensions = ['sphinx.ext.autodoc']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Platform'
copyright = u'2016, Cereson'
author = u'Cereson'
version = u'V1.0'
release = u'V1.0'
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'agogo'
html_static_path = ['_static']
htmlhelp_basename = 'Platformdoc'
latex_elements = {
}
latex_documents = [
    (master_doc, 'Platform.tex', u'Platform Documentation',
     u'Cereson', 'manual'),
]
man_pages = [
    (master_doc, 'platform', u'Platform Documentation',
     [author], 1)
]
texinfo_documents = [
    (master_doc, 'Platform', u'Platform Documentation',
     author, 'Platform', 'One line description of project.',
     'Miscellaneous'),
]


