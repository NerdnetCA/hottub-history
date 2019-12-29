

import os
import sys

import cherrypy


FILEROOT = os.path.dirname(__file__)

CODEPATH = os.path.join(FILEROOT,'app')
LIBPATH = os.path.join(FILEROOT,'lib')
TEMPLATEPATH = os.path.join(FILEROOT,'templates')

PREFIXPATH = '/tub'

if CODEPATH not in sys.path:
    sys.path.append(CODEPATH)
if LIBPATH not in sys.path:
    sys.path.append(LIBPATH)

CHERRYCONFIG = {
        '/' : {
            'tools.staticdir.root': FILEROOT,
            'tools.sessions.on': False,
            #'tools.sessions.storage_type': 'file',
            #'tools.sessions.storage_path': os.path.join(FILEROOT,'sessions'),
            #'tools.sessions.timeout': 60,
            #'error_page.404': handle_404,
            'environment': 'embedded'
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'static'
        }
    }

def app_init( instance ):
    return cherrypy.Application(instance, script_name=PREFIXPATH, config=CHERRYCONFIG)
