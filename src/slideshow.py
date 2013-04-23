import subprocess
class Slideshow:

	"Class to manage slideshow"

	def __init__(self, path):
		self.slide = None
		self.rootPath = path

	def isSlide(self):
		if self.slide is None:
			return False
		else:
			return True

	def start(self, path):
		path = self.rootPath+path
		self.slide = subprocess.Popen(["eog", "--slide-show", path])

	def stop(self):
		self.slide.terminate()
		self.slide = None