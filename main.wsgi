#!/usr/bin/python
#
# WSGI startup file for hottub-history
# created 2019-12-28 by colin
#
#

import config

# import the main application module
import app.tubhistory as tub
# and instantiate the application root class
app = tub.AppRoot()

# Wrap the app instance appropriately to be dispatched by our
# web server.  The server expects us to set a variable
# named 'application'
application = config.app_init( app , config.FILEROOT)

# Done.