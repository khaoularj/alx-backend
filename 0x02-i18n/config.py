#!/usr/bin/env python3
"""file to set Babel’s default locale
 ("en") and timezone ("UTC")"""


class Config(object):
    """class configuration for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
