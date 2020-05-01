#!/usr/bin/env python

from app import app as application
import sys
import site

site.addsitedir('/var/www/ChatBot/lib/python3.7/site-packages')
sys.path.insert(0, '/var/www/ChatBot')
