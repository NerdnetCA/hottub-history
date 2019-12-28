#!/usr/bin/python

import os
import config
import cherrypy


class AppRoot(object):
    def __init__(self):
        pass


if __name__=='__main__':
    cherrypy.quickstart( AppRoot(), config=config.CHERRYCONFIG)