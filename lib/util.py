def readConf():
	config = {}
	execfile("config.conf", config)
	return config

def test():
	print("test module")