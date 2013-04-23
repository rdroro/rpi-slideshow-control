from lib.bottle import route, run, template, static_file
import subprocess
import os
import lib.util as util
import logging	

config = util.readConf()
path = [{config["mediaFolder"]: "/"}]

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='front')

@route('/')
def hello():
	ls = os.listdir(config["mediaFolder"]);
	list_dir = []
	for fi in ls:
		if os.path.isdir(config["mediaFolder"]+fi):
			list_dir.append(fi)

	return template("front/views/index.html", ls=list_dir, path=path)


@route('/start/<folder:path>')
def start(folder):
	app_ar = list(config["app"])
	path = config["mediaFolder"]+folder
	app_ar.append(path)
	popen = subprocess.Popen(app_ar)
	return "OK"

@route('/info/<folder>')
def info(folder):
	p_path = list(path)
	p_path.append({folder: "/info/"+folder})

	ls = os.listdir(config["mediaFolder"]+folder)
	return template("front/views/info.html", ls=ls, path=p_path, folder = folder)


run(host=config["host"], port=config["port"], debug=True, reloader=True)

