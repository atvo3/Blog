#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'An'
SITENAME = 'Anvinski'
SITEURL = ''

PATH = 'content/'

TIMEZONE = 'US/Central'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# URL schema
# ARCHIVES_URL = 'all/archives/'
# ARCHIVES_SAVE_AS = 'all/archives/index.html'
# ARTICLE_URL = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
# ARTICLE_SAVE_AS = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
# AUTHOR_SAVE_AS = False
# AUTHORS_SAVE_AS = False
# CATEGORIES_URL = 'all/categories/'
# CATEGORIES_SAVE_AS = 'all/categories/index.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
  
# INDEX_SAVE_AS = 'all/index.html'
# INDEX_URL = 'all/'
# PAGE_URL = '{fullpath}/'
# PAGE_SAVE_AS = '{fullpath}/index.html'
# TAG_URL = 'all/tags/{slug}/'
# TAG_SAVE_AS = 'all/tags/{slug}/index.html'
# TAGS_URL = 'all/tags/'
# TAGS_SAVE_AS = 'all/tags/index.html'

# Filename metadata parsing
# FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'