

# region [Boilerplate]

import os
import sys
import time

sys.path.insert(0, os.path.abspath('.'))
import sphinx_bootstrap_theme
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
              #   'sphinx_copybutton',
              "sphinx_design",
              'sphinx.ext.autosectionlabel']


templates_path = ['_templates']

html_static_path = ['_static']


exclude_patterns = ["available_label.json", "extras/*"]


# get available styles via `pygmentize -L styles`
pygments_style = "dracula"

# endregion[Sphinx_Settings]

# region [Extension_Settings]

mermaid_params = ['--theme', 'forest', '--width', '2000', '--backgroundColor', 'transparent']
autosectionlabel_prefix_document = True
# endregion[Extension_Settings]

# region [HTML_Output_Settings]


html_theme = 'bootstrap'
html_theme_options = {"navbar_title": project,
                      "navbar_site_name": project}

if html_theme == "bootstrap":

    html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

    html_theme_options["bootswatch_theme"] = "Slate"


html_last_updated_fmt = "%Y/%B/%d"
html_permalinks_icon = ""
html_show_sourcelink = False
html_show_sphinx = False

html_sidebars = {
    '**': [
        'globaltoc.html'
    ]
}
# endregion[HTML_Output_Settings]
