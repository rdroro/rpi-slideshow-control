import os

class ListFile:

	def __init__(self, path):
		self.rootPath = path

	def list(self, path=""):
		ls = os.listdir(self.rootPath+path);
		list_dir = []
		for fi in ls:
			inspectFile = path+"/"+fi
			if os.path.isdir(self.rootPath+inspectFile):
				list_dir.append({"name": fi, "type":"dir", "link":inspectFile})
			else:
				list_dir.append({"name": fi, "type":"file", "link": inspectFile})
		return list_dir
