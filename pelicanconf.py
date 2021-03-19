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

DELETE_OUTPUT_DIRECTORY = True

PAGINATED_DIRECT_TEMPLATES = []

# URL schemas
ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = 'archives.html'

ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'

AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False

CATEGORIES_URL = 'categories/'
CATEGORIES_SAVE_AS = 'categories.html'

CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
  
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags.html'

TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
