#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from datetime import datetime
import os

AUTHOR = 'DPSG Stamm Sanssouci'
YEAR = datetime.now().year
SITENAME = 'DPSG Stamm Sanssouci'
SITEURL = 'http://www.pfadis-potsdam.de'

SITELOGO = '/images/logos/DPSG-Lilie_weiss.svg'
SITELOGO_SIZE = '20px'

PATH = 'content'
FILENAME_METADATA = '(?P<slug>.*)'

# pelican-bootstrap3
THEME = "./combined_theme"
BOOTSTRAP_THEME = "yeti"
CUSTOM_CSS = "theme/css/custom.css"
CUSTOM_JS = "theme/js/custom.js"
DIRECT_TEMPLATES = ('archives', 'tags', 'article_list')
PAGINATED_TEMPLATES = {'blog': None}
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_TAGS = True

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

PLUGIN_PATHS = ['../pelican-plugins/']
PLUGINS = [
  'liquid_tags.img', 
  'liquid_tags.video',
  'liquid_tags.youtube', 
  'liquid_tags.vimeo',
  'liquid_tags.include_code', 
  'twitter_bootstrap_rst_directives',
  'i18n_subsites'
]

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
I18N_TEMPLATES_LANG = 'de'
PADDED_SINGLE_COLUMN_STYLE = True

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feeds/all.rss"
TAG_FEED_ATOM = "feeds/tag_{slug}.atom.xml"
TAG_FEED_RSS = "feeds/tag_{slug}.rss"

MENUITEMS = (
  ('Biber', '/pages/biber.html'),
  ('Wölflinge', '/pages/wolflinge.html'),
  ('Jupfis', '/pages/jungpfadfinder.html'),
  ('Pfadis', '/pages/pfadfinder.html'),
  ('Rover', '/pages/rover.html'),
  ('Leiterrunde', '/pages/leiter.html'),
  # ('Mach mit!', '/pages/mitmachen.html'),
  # ('Blog', '/article_list.html'), # outdated
	('Impressum', '/pages/impressum.html')
)

DEFAULT_PAGINATION = False
TYPOGRIFY = True
# GOOGLE_ANALYTICS = "UA-55331241-2"

# Use Relative for (local) debugging, but Absolute for publishing
RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True

ROOT_FILES = 'root'

STATIC_PATHS = [
    'extra',
    ROOT_FILES,
    'images', 
]

EXTRA_PATH_METADATA = {
}

# Copy over files that should go into the root directory
rootFolder = os.path.join(PATH, ROOT_FILES)
for folder, dirs, files in os.walk(rootFolder):
  for filename in files:
    path = os.path.join(folder, filename)
    relativePath = os.path.relpath(path, rootFolder)
    contentPath = os.path.relpath(path, PATH)

    EXTRA_PATH_METADATA[contentPath.replace('\\', '/')] = {'path': relativePath.replace('\\', '/')}