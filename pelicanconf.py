#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = 'B Naylor'
SITENAME = 'Charlottesville Oral Histories'

SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'EN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 8

PLUGIN_PATHS = ["plugins","C:/Users/Beth/Documents/projects/pelican-plugins/"]
PLUGINS = ["liquid_tags.soundcloud","liquid_tags.youtube"]

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# NEW STUFF

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('about', '/about.html'),
    ('video', '/category/video.html'),
    ('audio', '/category/audio.html'),
    ('news','/category/news.html'),
    ('podcast', '/category/podcast.html'),
    ('resources','/category/resources.html'),
    ('contact','/contact.html')
    )

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
