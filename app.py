# set lib/ in current path
import sys
sys.path.append("lib/")
sys.path.append("src/")

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

config = util.readConf()
path = [{config["mediaFolder"]: "/"}]


sli = Slideshow(config["mediaFolder"])
fileO = ListFile(config["mediaFolder"])

# Route for static files like css, js or image
@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='front')

@app.route('/')
def hello():
	return list()


@app.route('/start/<folder:path>')
def start(folder):
	if sli.isSlide():
		print("Already in use")
		sli.stop()
	else:
		print("no slideshow")

	sli.start(folder)
	return "OK"

@app.route('/list/<folder:path>')
def list(folder="/"):
	if folder == "/":
		folder = ""

	list_dir = fileO.list(folder)
	return template("front/views/index.html", ls=list_dir, path=path)



run(app, host=config["host"], port=config["port"], debug=True, reloader=True)
#httpserver.serve(app, host=config["host"], port=config["port"])

