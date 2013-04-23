import subprocess
class Slideshow:

	"Class to manage slideshow"

	def __init__(self, program, path):
		self.slide = None
		self.rootPath = path
		self.programArgs = program

	def isSlide(self):
		if self.slide is None:
			return False
		else:
			return True

	def start(self, path):
		path = self.rootPath+path
		launch = list(self.programArgs)
		launch.append(path)
		self.slide = subprocess.Popen(launch)

	def stop(self):
		self.slide.terminate()
		self.slide = None