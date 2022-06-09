

# region [Boilerplate]

import os
import sys
import time

sys.path.insert(0, os.path.abspath('.'))
import sphinx_redactor_theme
# endregion [Boilerplate]

# region [Project_Info]

project = 'Gid Knowledge Vault'
project_copyright = f'{time.strftime("%Y")!s}, Giddi'
author = 'Giddi'


html_logo = "_images/main_logo.png"
html_favicon = "_images/main_favicon.png"

# endregion [Project_Info]

# region [Sphinx_Settings]

extensions = ["myst_parser",
              'sphinxcontrib.mermaid',
              'sphinxcontrib.images',
              "sphinxcontrib.fulltoc",
              "sphinx.ext.githubpages",
              'sphinx_copybutton',
              'sphinx.ext.autosectionlabel']


templates_path = ['_templates']

html_static_path = ['_static']


exclude_patterns = []


# get available styles via `pygmentize -L styles`
pygments_style = "solarized-light"

# endregion[Sphinx_Settings]

# region [Extension_Settings]

mermaid_params = ['--theme', 'forest', '--width', '2000', '--backgroundColor', 'transparent']
autosectionlabel_prefix_document = True
# endregion[Extension_Settings]

# region [HTML_Output_Settings]


html_theme = 'sphinx_redactor_theme'
html_theme_path = [sphinx_redactor_theme.get_html_theme_path()]
html_theme_options = {}


html_last_updated_fmt = "%Y/%B/%d"
html_permalinks_icon = ""
html_show_sourcelink = False
html_show_sphinx = False

html_sidebars = {
    '**': [
        'globaltoc.html',
        'searchbox.html',
    ]
}

# endregion[HTML_Output_Settings]
