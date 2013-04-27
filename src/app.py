# set lib/ in current path
import sys

generalPath = sys.argv[1]

sys.path.append(generalPath+"/lib/")
sys.path.append(generalPath+"/src/")

import subprocess
import os
import logging	

from bottle import Bottle, route, run, template, static_file, redirect
from paste import httpserver
import util
from slideshow import Slideshow
from listFile import ListFile

# Bottle app initialization
app = Bottle()

config = {}
execfile(generalPath+"conf/config.conf", config)


sli = Slideshow(config["app"], config["mediaFolder"])
fileO = ListFile(config["mediaFolder"])

webapp = generalPath+"webapp/"




################
# Bottle Begin #
################

# Route for static files like css, js or image
@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=webapp)

# root route
@app.route('/')
def hello():
	return list()

@app.route('/start/')
def startRoot():
	return start()

# route to start slideshow
@app.route('/start/<folder:path>')
def start(folder="/"):
	if sli.isSlide():
		sli.stop()

	sli.start(folder)
	# return list(mediaFolder)
	redirect("/")

# Route to list contents of directory
@app.route('/list/<folder:path>')
def list(folder="/"):
	breadcrumb  = [{"name":config["mediaFolder"], "url": "/"}]
	if folder == "/":
		folder = ""
	else:
		breadcrumb.append({"name": folder, "url": folder})

	list_dir = fileO.list(folder)
	return template(webapp+"views/index.html", ls=list_dir, breadcrumb=breadcrumb, baseurl=generalPath, currentFolder=folder)

if config['mode'] == "dev":
	run(app, host=config["host"], port=config["port"], debug=True, reloader=True)
else:
	httpserver.serve(app, host=config["host"], port=config["port"])

