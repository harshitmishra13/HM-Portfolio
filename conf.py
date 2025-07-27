import os
import sys
from pathlib import Path
from typing import Any, Dict
import pydata_sphinx_theme

# -- Project information -----------------------------------------------------
project = "Harshit Mishra Portfolio"
author  = "Harshit Mishra"
release = "2025"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx_design",
    "sphinxcontrib.youtube",
    "sphinx_copybutton",
    "sphinx.ext.todo",
]


templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme       = "pydata_sphinx_theme"
html_static_path = ['_static']
html_show_sphinx = False  # Hides "Created using Sphinx"

html_theme_options = {
    # ... your existing options like logo, icon_links, etc.
    
    # Disable sidebars (both left nav and right TOC)
    "show_nav_level": 0,
    "navigation_with_keys": False,  # disables left/right keyboard nav
    "header_links_before_dropdown": 4,  # optional tweak
    
    "show_toc_level": 0,  # disables in-page section navigation (right sidebar)
    
    # Remove sidebar completely
    "primary_sidebar_end": [],
    "secondary_sidebar_items": [],
}

html_theme_options = {
    # ... your existing settings

    "show_toc_level": 0  # 👈 disables "On this page" (right sidebar)
}

html_show_sourcelink = False
html_copy_source = False

html_sidebars = {
    "**": []
}

html_theme_options = {
    "logo": {"text": "Harshit Mishra Portfolio"},
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["navbar-icon-links", "theme-switcher"],
    "icon_links": [
        {
            "name": "YouTube",
            "url": "https://youtube.com/@harshittmishraa",
            "icon": "fab fa-youtube",
        },
        {
            "name": "Instagram",
            "url": "https://instagram.com/harshittmishraa",
            "icon": "fab fa-instagram",
        },
        {
            "name": "X",
            "url": "https://x.com/theharshitM",
            "icon": "fab fa-twitter",
        },
        {
            "name": "LinkedIn",
            "url": "https://linkedin.com/in/harshitmishra13",
            "icon": "fab fa-linkedin",
        },
    ],

    # ✅ This removes the default theme footer parts
    "footer_start": [],  # removes "Built with PyData Sphinx Theme..."
    "footer_end": [],

}

html_static_path = ['_static']
html_css_files = [
    'custom.css',
]
