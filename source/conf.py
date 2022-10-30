

# region [Boilerplate]

import os
import sys
import time

sys.path.insert(0, os.path.abspath('.'))

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
              "sphinxcontrib.fulltoc",
              "sphinx.ext.githubpages",
              'sphinx_copybutton',
              'sphinx.ext.autosectionlabel']


templates_path = ['_templates']

html_static_path = ['_static']
html_css_files = [
    'css/extra_styling.css',
]

exclude_patterns = []


# get available styles via `pygmentize -L styles`
pygments_style = "tomorrow-night-eighties"

# endregion[Sphinx_Settings]

# region [Extension_Settings]

mermaid_params = ['--theme', 'forest', '--width', '2000', '--backgroundColor', 'transparent']
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 1
# endregion[Extension_Settings]

# region [HTML_Output_Settings]


html_theme = 'alabaster'
html_theme_path = []
html_theme_options = {"page_width": 1500, "body_max_width": None}


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


html_context = {"base_css_name": html_theme}
# endregion[HTML_Output_Settings]
