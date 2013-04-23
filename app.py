# set lib/ in current path
import sys
sys.path.append("lib/")
sys.path.append("src/")

import subprocess
import os
import logging	

from bottle import Bottle, route, run, template, static_file
from paste import httpserver
import util
from slideshow import Slideshow

# Bottle app initialization
app = Bottle()

config = util.readConf()
path = [{config["mediaFolder"]: "/"}]


sli = Slideshow(config["mediaFolder"])

# Route for static files like css, js or image
@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='front')

@app.route('/')
def hello():
	ls = os.listdir(config["mediaFolder"]);
	list_dir = []
	for fi in ls:
		if os.path.isdir(config["mediaFolder"]+fi):
			list_dir.append(fi)

	return template("front/views/index.html", ls=list_dir, path=path)


@app.route('/start/<folder:path>')
def start(folder):
	if sli.isSlide():
		print("Already in use")
		sli.stop()
	else:
		print("no slideshow")

	sli.start(folder)
	return "OK"

@app.route('/info/<folder>')
def info(folder):
	p_path = list(path)
	p_path.append({folder: "/info/"+folder})

	ls = os.listdir(config["mediaFolder"]+folder)
	return template("front/views/info.html", ls=ls, path=p_path, folder = folder)


run(app, host=config["host"], port=config["port"], debug=True, reloader=True)
#httpserver.serve(app, host=config["host"], port=config["port"])

