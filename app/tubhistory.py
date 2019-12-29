#!/usr/bin/python

import os
import config
import cherrypy

import app.chlorinate

class AppRoot(object):
    """This is the application's entrypoint class.
    """

    def __init__(self):
        """Set up all of the subpaths we need and connect
        them to appropriate handler instances.

        /chlorinate points to the handler for entering a chlorination event.
        """
        self.chlorinate = app.chlorinate.Chlorinate()
        pass

    @cherrypy.expose()
    #@lib.templater.Templater('start.xml')
    def index(self, *args, **kws):
        """Main entrypoint - this is where users are expected to begin
        their interaction with the app.

        :return: the application, rendered as HTML 5
        """
        return str('<b>tubhistory.index</b><a href="{0}">netsr</a>'.format(config.PREFIXPATH))

    @cherrypy.expose()
    def default(self, *args, **kws):
        return args[0]

# If this file is executed directly by the interpreter
# (e.g. by entering "python tubhistory.py"), then start
# the application in cherrypy's standalone web server.
# If not, then simply defining the AppRoot class is all
# we need to do here.
if __name__=='__main__':
    cherrypy.quickstart( AppRoot(), config=config.CHERRYCONFIG)

